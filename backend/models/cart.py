#!/usr/bin/python3
""" holds class Category"""
from backend.models.shared import SharedBase, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Cart(SharedBase, Base):
    """ cart table """
    __tablename__ = 'cart'
    # One-to-One Relationship (1 user to on cart)
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="cart")
    # One-to-Many Relationship (1 cart to many cart_items)
    cart_items = relationship("CartItem", back_populates="cart")
