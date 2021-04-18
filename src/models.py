from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.username,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):

    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)
    films = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120),unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    homeworld = db.Column(db.String(120), unique=False, nullable=False)
    mass= db.Column(db.String(120), unique=False, nullable=False)
    name= db.Column(db.String(120), unique=False, nullable=False)
    skin_color = db.Column(db.String(120), unique=False, nullable=False)
    created = db.Column(db.String(120), unique=False, nullable=False)
    edited = db.Column(db.String(120), unique=False, nullable=False)
    species = db.Column(db.String(120), unique=False, nullable=False)
    starships = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=False, nullable=False)
    vehicles = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.people_id

    def serialize(self):
        return {
            "people_id": self.people_id,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "films" : self.films,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "mass": self.mass,
            "name": self.name,
            "skin_color":  self.skin_color,
            "created": self.created,
            "edited":  self.edited,
            "species": self.species,
            "starships": self.starships,
            "url": self.url,
            "vehicles": self.vehicles
        }

    
class Planets(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    created = db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.String(120), unique=False, nullable=False)
    edited = db.Column(db.String(120), unique=False, nullable=False)
    films = db.Column(db.String(120), unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    orbital_period = db.Column(db.String(120), unique=False, nullable=False)
    population= db.Column(db.String(120), unique=False, nullable=False)
    residents= db.Column(db.String(120), unique=False, nullable=False)
    rotation_period = db.Column(db.String(120), unique=False, nullable=False)
    surface_water = db.Column(db.String(120), unique=False, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=False, nullable=False)
    starships = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.id
    def serialize(self):
        return {
            "climate": self.climate,
            "created": self.created,
            "diameter": self.diameter,
            "edited" : self.edited,
            "films": self.films,
            "gravity": self.gravity,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "residents":  self.residents,
            "rotation_period": self.rotation_period,
            "surface_water":  self.surface_water,
            "terrain": self.terrain,
            "url": self.url,
            "starships": self.starships

        }

class FavsUser(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    fav_name= db.Column(db.String(120), unique=False, nullable=False)


    def __repr__(self):
        return '<Favs User %r>' % self.people_id
        
    def serialize(self):
        return {
            "fav_name": self.fav_name,
        }


    


