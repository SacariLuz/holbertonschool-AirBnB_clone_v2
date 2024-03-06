#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from os import environ
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class for ORM"""
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
else:
    class State(BaseModel):
        """ State class """
        name = ''

        @property
        def cities(self):
            from models import storage
            list_cities = []

            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)

            return list_cities
