from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.username,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, ForeignKey('FavPeople.people_id'))
    people_id = db.Column(db.String, primary_key=True)
    birth_year = db.Column(db.String, primary_key=True)
    eye_color = db.Column(db.String, primary_key=True)
    films = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String, primary_key=True)
    hair_color = db.Column(db.String, primary_key=True)
    height = db.Column(db.String, primary_key=True)
    homeworld = db.Column(db.String, primary_key=True)
    mass= db.Column(db.String, primary_key=True)
    name= db.Column(db.String, primary_key=True)
    skin_color = db.Column(db.String, primary_key=True)
    created = db.Column(db.String, primary_key=True)
    edited = db.Column(db.String, primary_key=True)
    species = db.Column(db.String, primary_key=True)
    starships = db.Column(db.String, primary_key=True)
    url = db.Column(db.String, primary_key=True)
    vehicles = db.Column(db.String, primary_key=True)

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
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, ForeignKey('FavPlanet.people_id'))
    climate = db.Column(db.String, primary_key=True)
    created = db.Column(db.String, primary_key=True)
    diameter = db.Column(db.String, primary_key=True)
    edited = db.Column(db.String, primary_key=True)
    films = db.Column(db.String, primary_key=True)
    gravity = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, primary_key=True)
    orbital_period = db.Column(db.String, primary_key=True)
    population= db.Column(db.String, primary_key=True)
    residents= db.Column(db.String, primary_key=True)
    rotation_period = db.Column(db.String, primary_key=True)
    surface_water = db.Column(db.String, primary_key=True)
    terrain = db.Column(db.String, primary_key=True)
    url = db.Column(db.String, primary_key=True)
    starships = db.Column(db.String, primary_key=True)

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

class FavPeople(db.Model):
    __tablename__ = 'FavPeople'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

    def __repr__(self):
        return '<Fav People %r>' % self.people_id
        
    def serialize(self):
        return {
            "people_id": self.people_id,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }

class FavPlanet(db.Model):
    __tablename__ = 'FavPlanet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    people_id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'))


    def __repr__(self):
        return '<Fav Planet %r>' % self.people_id
        
    def serialize(self):
        return {
            "people_id": self.people_id,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }
    


