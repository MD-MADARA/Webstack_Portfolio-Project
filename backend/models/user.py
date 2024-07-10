#!/usr/bin/python3
""" holds User Model"""
from backend.models.shared import SharedBase, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(SharedBase, Base):
    """User Table """
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    address = Column(String(256), nullable=False)
    phone = Column(String(128), nullable=False)
    # One-to-One Relationship (1 user to on cart)
    cart = relationship("Cart", uselist=False, back_populates="user", cascade="all, delete-orphan")
    # One-to-Many Relationship (1 user to many orders)
    orders = relationship("Order", back_populates="user")

    def __setattr__(self, key, value):
        """sets a password with md5 encryption"""
        if key == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(key, value)
