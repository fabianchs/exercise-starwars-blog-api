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

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def handle_hello():

    people=Characters.query.all()
    all_people = list(map(lambda x: x.serialize(), people))

    return jsonify(all_people), 200


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

@app.route('/favs', methods=['GET'])
def handle_favs():

    favs=FavsUser.query.all()
    all_favs= list(map(lambda x: x.serialize(), favs))

    return jsonify(all_favs), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
