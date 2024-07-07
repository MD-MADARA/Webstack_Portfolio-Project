#!/usr/bin/python3
"""This module defines a shared class for all models"""
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SharedBase:
    """A base class for all models"""

    id = Column(Integer, primary_key=True, autoincrement=True)

    created_date = Column(DateTime, default=datetime.now(), nullable=False)

    updated_date = Column(DateTime, default=datetime.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of the Shared class model"""
        if kwargs:
            time = '%Y-%m-%dT%H:%M:%S.%f'
            if kwargs.get("created_date", None) and type(self.created_date) is str:
                self.created_date = datetime.strptime(kwargs["created_date"], time)
            else:
                self.created_date = datetime.now()
            if kwargs.get("updated_date", None) and type(self.updated_date) is str:
                self.updated_date = datetime.strptime(kwargs["updated_date"], time)
            else:
                self.updated_date = datetime.now()
            for key, value in kwargs.items():
                if key not in ["__class__", "created_date", "updated_date"]:
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
