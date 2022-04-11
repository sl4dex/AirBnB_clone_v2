#!/usr/bin/python3
"""
New engine DBStorage: (models/engine/db_storage.py)
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


class DBStorage():
    """class dbstorage"""
    __engine = None
    __session = None

    def __init__(self):
        """init for DBStorage"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.
                format(
                    getenv(HBNB_MYSQL_USER),
                    getenv(HBNB_MYSQL_PWD),
                    getenv(HBNB_MYSQL_HOST),
                    getenv(HBNB_MYSQL_DB)),
                pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.__session = Session()
        if getenv(HBNB_ENV) is 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """
        returns the dictionary __objects
        """
        all_items = {}
        if cls is not None:
            todos = self.__session.query(cls)
        else:
            todos = self.__session.query()
        for item in todos:
            key = 'cls' + '.' + str(self.id)
            all_items.update(key = item)
        return all_items
