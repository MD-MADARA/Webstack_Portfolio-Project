#!/usr/bin/python3
""" holds class Category"""
from backend.models.shared import SharedBase, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class CartItem(SharedBase, Base):
    """ cartItem table """
    __tablename__ = 'cartItem'
    product_id = Column(String(128), ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False, default=1)
    # One-to-Many Relationship (1 cart to many cartItems)
    cart_id = Column(String(128), ForeignKey('cart.id'))
    cart = relationship("Cart", back_populates="cart_items")
    # One-to-Many Relationship (1 order to many cartItems)
    order_id = Column(String(128), ForeignKey('orders.id'))
    order = relationship("Order", back_populates="items")
