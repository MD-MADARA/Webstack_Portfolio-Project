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
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    order_items = relationship(
        "OrderItem",
        backref="order",
        cascade="all, delete, delete-orphan"
    )
