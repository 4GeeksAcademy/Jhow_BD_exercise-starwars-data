import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(250), unique=True, nullable=False)
    firstname = Column(String(70) )
    lastname = Column(String(60) )
    address = Column(String(80) )
    phone = Column(String(80) )
    password = Column(String(60) )
    email = Column(String(250), unique=True,  nullable=False)

    likes = relationship('Likes', back_populates='user')

#ok
class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), unique=True, nullable=False)
    gravedad = Column(String(70))
    diametro = Column(String(60))
    poblacion = Column(String(80))
    descripcion = Column(String(220))
#
    planetas = relationship('Likes', back_populates='planetas')
    
#ok
class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), unique=True, nullable=False)
    peso = Column(String(70) )
    color_ojos = Column(String(60) )
    sexo = Column(Enum('Hombre','Mujer','No definido'), nullable=False)
    color_pelo = Column(String(50) )

    personajes = relationship('Likes', back_populates='personajes')

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_planetas = Column(Integer, ForeignKey('planetas.id'), primary_key=True)
    id_personajes = Column(Integer, ForeignKey('personajes.id'), primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), primary_key=True)

    user = relationship('User', back_populates='likes')
    planetas = relationship('Planetas', back_populates='likes')
    personajes = relationship('Personajes', back_populates='likes')
   
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
