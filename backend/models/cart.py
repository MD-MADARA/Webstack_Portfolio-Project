#!/usr/bin/python3
""" holds class Category"""
from backend.models.shared import SharedBase, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

association_table = Table('association_table', Base.metadata,
    Column('cart_id', String(128), ForeignKey('cart.id')),
    Column('product_id', String(128), ForeignKey('products.id'))
)

class Cart(SharedBase, Base):
    """ cart table """
    __tablename__ = 'cart'
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    products = relationship('Product', secondary='association_table')
