#!/usr/bin/python3
"""This module defines a shared class for all models"""
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base
from uuid import uuid4


Base = declarative_base()


class SharedBase:
    """A base class for all models"""


    id = Column(String(128), primary_key=True, default=str(uuid4()))

    created_date = Column(DateTime, default=datetime.now(), nullable=False)

    updated_date = Column(DateTime, default=datetime.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of the Shared class model"""

        for key, value in kwargs.items():
            ignore = ["__class__", "created_date", "updated_date", "id", "discount"]
            if key not in ignore:
                if hasattr(self, key):
                    setattr(self, key, value)

    def save(self):
        """Updates updated_date with current time when instance is changed"""
        from backend import storage
        self.updated_date = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        from backend import storage
        storage.delete(self)

    def dict_format(self):
        """Convert instance into dictionnary format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        if "password" in dictionary:
            del dictionary["password"]
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]

        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = datetime.isoformat(value)
        return dictionary
