#!/usr/bin/python3
""" StorageEngine module
"""

from backend.data_models.shared import Base
from backend.data_models.order_items import OrderItem
from backend.data_models.order import Order
from backend.data_models.product import Product
from backend.data_models.user import User
from backend.data_models.cart import Cart
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



class StorageEngine:
    """ Engine class to controle and interacts with MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instatntiates database engine"""
        user = getenv('DB_USER')
        password = getenv('DB_PASSWORD')
        host_name = getenv('HOST_NAME')
        db_name = getenv('DB_NAME')
        db_url = f"mysql+mysqldb://{user}:{password}@{host_name}/{db_name}"

        self.__engine = create_engine(db_url, pool_pre_ping=True)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
