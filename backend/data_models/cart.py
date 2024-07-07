#!/usr/bin/python3
""" holds class Category"""
from data_models.shared import SharedBase, Base
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

association_table = Table('association_table', Base.metadata,
    Column('cart_id', Integer, ForeignKey('cart.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

class Cart(SharedBase, Base):
    """ cart table """
    __tablename__ = 'cart'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    products = relationship('Product', secondary='association_table')
