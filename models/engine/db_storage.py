#!/usr/bin/python3
"""
New engine DBStorage: (models/engine/db_storage.py)
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
from os import getenv
from models.state import State
from models.city import City
from models.base_model import BaseModel, Base


class DBStorage():
    """class dbstorage"""
    __engine = None
    __session = None

    def __init__(self):
        """init for DBStorage"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.
                format(
                    getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def close(self):
        """close session"""
        self.__session.close()

    def all(self, cls=None):
        """
        returns the dictionary __objects
        """
        from console import HBNBCommand
        all_items = {}
        if cls is not None:
            todos = self.__session.query(cls).all()
        else:
            clases = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            for clase in clases:
                todos = self.__session.query(clase).all()
        for item in todos:
            key = (item.__class__.__name__) + '.' + (item.id)
            all_items[key] = item
        return all_items

    def new(self, obj):
        """add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create the current database session and create all tables """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
                sessionmaker(self.__engine, expire_on_commit=False))
        self.__session = Session()
