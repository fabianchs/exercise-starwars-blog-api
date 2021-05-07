"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, FavsUser, Characters, Planets
#from models import Person

#import JWT for tokenization
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# config for jwt
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Correo o contraseña incorrectos"}), 401

    
    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400

    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Invalid username or password"}), 401
    else:
        print(user)
        # create a new token with the user id inside
        access_token = create_access_token(identity=user.id)
        return jsonify({ "token": access_token, "user_id": user.id }), 200


@app.route('/register', methods=['POST'])
def register_user():

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400
    
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return jsonify({"msg": "User already exists"}), 401
    else:
        new_user = User()
        new_user.email = email
        new_user.password = password

        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 200

@app.route('/people', methods=['GET'])
def handle_people():

    people=Characters.query.all()
    all_people = list(map(lambda x: x.serialize(), people))

    return jsonify(all_people), 200

@app.route("/hello", methods=["POST"])
@jwt_required()
def create_hello():

    dictionary= {"message" : "hello world"}
    return jsonify(dictionary)


@app.route('/people/<int:people_id>', methods=['GET'])
def handle_one_character(people_id):

    character = Characters.query.filter_by(id=people_id)#Este se utiliza para serializar el character
    character_exception = Characters.query.get(people_id)#Este se utiliza para evaluar si el character existe

    # map the results and your list of people  inside of the all_people variable
    ch_description = list(map(lambda x: x.serialize(), character))#Carga descripción serializada para pasarle jsonify

    if character_exception is None:
        raise APIException('Character not found, try again please', status_code=404)
    else:
        return jsonify(ch_description), 200

@app.route('/newcharacter/', methods=['POST'])
def new_char():

    request_body=request.get_json()
    
    new_char = Characters(birth_year=request_body["birth_year"], eye_color=request_body["eye_color"], gender=request_body["gender"], hair_color=request_body["hair_color"], height=request_body["height"], homeworld=request_body["homeworld"], mass=request_body["mass"], name=request_body["name"], skin_color=request_body["skin_color"], created=request_body["created"], edited=request_body["edited"], url=request_body["url"])

    db.session.add(new_char)
    db.session.commit()

    return jsonify("Character added correctly"), 200

@app.route('/planets', methods=['GET'])
def handle_planets():

    planets=Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))

    return jsonify(all_planets), 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def handle_one_planet(planet_id):

    planet = Planets.query.filter_by(id=planet_id)#Este se utiliza para serializar el character
    planet_exception = Planets.query.get(planet_id)#Este se utiliza para evaluar si el character existe

    # map the results and your list of people  inside of the all_people variable
    pl_description = list(map(lambda x: x.serialize(), planet))#Carga descripción serializada para pasarle jsonify

    if planet_exception is None:
        raise APIException('Planet not found, try again please', status_code=404)
    else:
        return jsonify(pl_description), 200

@app.route('/newplanet/', methods=['POST'])
def new_plan():

    request_body=request.get_json()
    
    new_planet = Planets(climate=request_body["climate"], diameter=request_body["diameter"], edited=request_body["edited"], gravity=request_body["gravity"], name=request_body["name"], orbital_period=request_body["orbital_period"], population=request_body["population"], rotation_period=request_body["rotation_period"], surface_water=request_body["surface_water"], terrain=request_body["terrain"], url=request_body["url"])

    db.session.add(new_planet)
    db.session.commit()

    return jsonify("Planet added correctly"), 200

@app.route('/favs', methods=['GET'])
def handle_favs():

    favs=FavsUser.query.all()
    all_favs= list(map(lambda x: x.serialize(), favs))

    return jsonify(all_favs), 200

@app.route('/newfav/', methods=['POST'])
def new_fav():

    request_body=request.get_json()
    
    new_fav = FavsUser(fav_name=request_body["fav_name"])

    db.session.add(new_fav)
    db.session.commit()

    return jsonify("Favorite added correctly"), 200

@app.route('/delfav/<int:fav_id>', methods=['DELETE'])
def del_fav(fav_id):

    fav_obtained = FavsUser.query.get(fav_id)

    if fav_obtained is None:
        raise APIException('Favorite not found', status_code=404)
    else:
        db.session.delete(fav_obtained)
        db.session.commit()
        return jsonify("Favorite deleted correctly"), 200

@app.route('/delallplanets', methods=['DELETE'])
def del_plan():

    Planets.query.delete()
    db.session.commit()

    return jsonify("All planets were deleted"), 200

@app.route('/delallcharacters', methods=['DELETE'])
def del_char():

    Characters.query.delete()
    db.session.commit()

    return jsonify("All characters were deleted"), 200
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

