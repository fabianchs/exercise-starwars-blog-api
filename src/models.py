from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

class FavPeople(db.Model):
    __tablename__ = 'FavPeople'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

class FavPlanet(db.Model):
    __tablename__ = 'FavPlanet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    people_id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'))

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
    crated = db.Column(db.String, primary_key=True)
    edited = db.Column(db.String, primary_key=True)
    species = db.Column(db.String, primary_key=True)
    starships = db.Column(db.String, primary_key=True)
    url = db.Column(db.String, primary_key=True)
    vehicles = db.Column(db.String, primary_key=True)
    
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
            "email": self.email,
            # do not serialize the password, its a security breach
        }
