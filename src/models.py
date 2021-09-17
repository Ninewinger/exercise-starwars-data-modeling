import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique= True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique= True)
    loginStatus = Column(String(50), nullable=False)
    favorites = Column(Integer, ForeignKey('Favorite.id'))

    def verifyLogin(self):
        return {}

class Favorite(Base):
    __tablename__ = 'Favorite'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('Planets.id'))
    character_id = Column(Integer, ForeignKey('Characters.id'))

class Planets(Base):
    __tablename__= "Planets"
    id = Column(Integer, primary_key = True)
    diameter = Column(String(250))
    size = Column(String(250))
    atmosphere = Column(String(250))
    temperature = Column(String(250))
  
class Characters(Base):
    __tablename__= "Characters"
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    age = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')