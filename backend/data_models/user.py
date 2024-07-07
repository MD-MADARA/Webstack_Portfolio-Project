#!/usr/bin/python3
""" holds User Model"""
from backend.data_models.shared import SharedBase, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5


class User(SharedBase, Base):
    """User Table """
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    address = Column(String(256), nullable=False)
    phone = Column(String(128), nullable=False)
    cart_id = Column(Integer, ForeignKey('cart.id'))
    orders = relationship("Order", backref="user", cascade="all, delete, delete-orphan")

    
    def __setattr__(self, key, value):
        """sets a password with md5 encryption"""
        if key == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(key, value)
