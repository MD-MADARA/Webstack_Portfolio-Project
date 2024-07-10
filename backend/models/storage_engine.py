#!/usr/bin/python3
""" StorageEngine module
"""

from backend.models.shared import Base
from backend.models.order import Order
from backend.models.product import Product
from backend.models.user import User
from backend.models.cart import Cart
from backend.models.cart_item import CartItem
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {
    "Product": Product, "Order": Order,
    "User": User, "Cart": Cart, "CartItem": CartItem
}


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


    def count(self, cls=None):
        """count all classes"""
        cpt = 0
        for clss in classes:
            if cls is None or cls is classes[clss]:
                objs = self.__session.query(classes[clss]).all()
                cpt += len(objs)
        return cpt

    def get_by_id(self, cls, id):
        """get object by class and id"""
        for clss in classes:
            if cls is classes[clss]:
                result = self.__session.query(cls).filter(cls.id == id).first()
                if result:
                    return result
        return None

    def get_user_by_email(self, email):
        """get user by email"""
        user = self.__session.query(User).filter(User.email == email).first()
        if user:
            return user
        return None

    def all(self, cls, order_asc=None, order_desc=None, filter=None):
        """
        Query on the current database session for a specific class (cls).
        
        :param cls: The class of the objects to be queried.
        :param order_asc: Attribute name to order the results in ascending order.
        :param order_desc: Attribute name to order the results in descending order.
        :param filter: Dictionary of attributes and their values to filter the results.
        
        :return: Dictionary of objects of the specified class.
        """
        query = self.__session.query(cls)
        
        # Apply filtering
        if filter:
            for attr, value in filter.items():
                if hasattr(cls, attr):
                    query = query.filter(getattr(cls, attr) == value)
                if attr == 'max_price' and cls is Product:
                    query = query.filter(Product.price <= value)
                if attr == 'min_price' and cls is Product:
                    query = query.filter(Product.price >= value)

        # Apply ordering
        if order_asc and hasattr(cls, order_asc):
            query = query.order_by(getattr(cls, order_asc))
        elif order_desc and hasattr(cls, order_desc):
            query = query.order_by(getattr(cls, order_desc).desc())

        # Execute the query and fetch all results
        objs = query.all()

        # Construct a dictionary of objects with a custom key format
        new_dict = {f'(N°{i}) {obj.__class__.__name__}.{obj.id}': obj for i, obj in enumerate(objs, start=1)}
        return new_dict

    def refresh(self, obj):
        """Reloads the Instance state"""
        self.__session.refresh(obj)
