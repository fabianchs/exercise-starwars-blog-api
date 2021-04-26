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
    birth_year = db.Column(db.String(120), unique=False, nullable=True)
    eye_color = db.Column(db.String(120), unique=False, nullable=True)
    gender = db.Column(db.String(120),unique=False, nullable=True)
    hair_color = db.Column(db.String(120), unique=False, nullable=True)
    height = db.Column(db.String(120), unique=False, nullable=True)
    homeworld = db.Column(db.String(120), unique=False, nullable=True)
    mass= db.Column(db.String(120), unique=False, nullable=True)
    name= db.Column(db.String(120), unique=False, nullable=True)
    skin_color = db.Column(db.String(120), unique=False, nullable=True)
    created = db.Column(db.String(120), unique=False, nullable=True)
    edited = db.Column(db.String(120), unique=False, nullable=True)
    url = db.Column(db.String(120), unique=False, nullable=True)


    def __repr__(self):
        return '<Characters %r>' % self.people_id

    def serialize(self):
        return {
            "internal_id": self.id,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "mass": self.mass,
            "name": self.name,
            "skin_color":  self.skin_color,
            "created": self.created,
            "edited":  self.edited,
            "url": self.url,
        }

    
class Planets(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String(120), unique=False, nullable=True)
    created = db.Column(db.String(120), unique=False, nullable=True)
    diameter = db.Column(db.String(120), unique=False, nullable=True)
    edited = db.Column(db.String(120), unique=False, nullable=True)
    gravity = db.Column(db.String(120), unique=False, nullable=True)
    name = db.Column(db.String(120), unique=False, nullable=True)
    orbital_period = db.Column(db.String(120), unique=False, nullable=True)
    population= db.Column(db.String(120), unique=False, nullable=True)
    rotation_period = db.Column(db.String(120), unique=False, nullable=True)
    surface_water = db.Column(db.String(120), unique=False, nullable=True)
    terrain = db.Column(db.String(120), unique=False, nullable=True)
    url = db.Column(db.String(120), unique=False, nullable=False)


    def __repr__(self):
        return '<Planets %r>' % self.id
    def serialize(self):
        return {
            "internal_id": self.id,
            "climate": self.climate,
            "created": self.created,
            "diameter": self.diameter,
            "edited" : self.edited,
            "gravity": self.gravity,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "surface_water":  self.surface_water,
            "terrain": self.terrain,
            "url": self.url,
        }

class FavsUser(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    fav_name= db.Column(db.String(120), unique=False, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, foreign_keys=[id_user])


    def __repr__(self):
        return '<Favs User %r>' % self.people_id
        
    def serialize(self):
        return {
            "internal_id": self.id,
            "fav_name": self.fav_name,
            "id_user" :self.id_user
        }


    


