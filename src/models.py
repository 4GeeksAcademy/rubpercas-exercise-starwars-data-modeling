import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(150))
    favorite = relationship('Favorite', back_populates='User')

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates='Favorite')

    character_id = Column(Integer, ForeignKey('Character.id'))
    character = relationship('Character', back_populates='Favorite')

    planet_id = Column(Integer, ForeignKey('Planet.id'))
    planet = relationship('Planet', back_populates='Favorite')

    vehicle_id = Column(Integer, ForeignKey('Vehicle.id'))
    vehicle = relationship('Vehicle', back_populates='Favorite')

class Character(Base):
    __tablename__ = 'Character'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    gender = Column(String(15))
    birth_date = Column(String(100))
    description = Column(String(500), nullable=False)
    url = Column(String(150), nullable=False)

    planet_id = Column(Integer, ForeignKey('Planet.id'))
    planet = relationship('Planet', back_populates='Character')

    favorite = relationship('Favorite', back_populates='Character')
    vehicle = relationship('Vehicle', back_populates='Character')

class Planet(Base):
    __tablename__ = 'Planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(500), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(50))

    favorite = relationship('Favorite', back_populates='Planet')
    character = relationship('Character', back_populates='Planet')

class Vehicle(Base):
    __tablename__ = 'Vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    model = Column(String(100))
    description = Column(String(500), nullable=False)
    capacity = Column(Integer, nullable=False)

    character_id = Column(Integer, ForeignKey('Character.id'))
    character = relationship('Character', back_populates='Vehicle')

    favorite = relationship('Favorite', back_populates='Vehicle')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
