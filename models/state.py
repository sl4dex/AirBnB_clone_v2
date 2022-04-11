#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete-orphan")

    @property
    def cities(self):
        """
        returns the list of City instances with state_id
        equals to the current State.id
        """
        city_list = []
        all_cities = storage.all(City)
        for one_city in all_cities:
            if state_id is self.id:
                city_list.append(one_city)
        return city_list
