#!/usr/bin/python3
"""This module defines a shared class for all models"""
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base
from uuid import uuid4

Base = declarative_base()


class SharedBase:
    """A base class for all models"""


    id = Column(String(128), primary_key=True)

    created_date = Column(DateTime, nullable=False)

    updated_date = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of the Shared class model"""

        self.id = str(uuid4())
        self.created_date = datetime.now(timezone.utc)
        self.updated_date = datetime.now(timezone.utc)

        for key, value in kwargs.items():
            ignore = ["__class__", "created_date", "updated_date", "discount"]
            if key not in ignore:
                if hasattr(self, key):
                    setattr(self, key, value)

    def save(self):
        """Updates updated_date with current time when instance is changed"""
        from backend import storage
        self.updated_date = datetime.now(timezone.utc)
        storage.new(self)
        storage.save()
        storage.refresh(self)

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
