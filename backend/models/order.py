#!/usr/bin/python3
""" Order model"""
from backend.models.shared import SharedBase, Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Order(SharedBase, Base):
    """ Order Table """
    __tablename__ = 'orders'
    total_price = Column(Float, nullable=False, default=0)
    status = Column(String(50), nullable=False, default="pending")

    # One-to-Many Relationship (1 user to many orders)
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="orders")

    # One-to-Many Relationship (1 order to many cartItems)
    items = relationship("CartItem", uselist=True)
