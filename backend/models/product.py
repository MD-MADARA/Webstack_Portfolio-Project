#!/usr/bin/python3
""" holds class User"""
from backend.models.shared import SharedBase, Base
from sqlalchemy import Column, String, Integer, CheckConstraint, Float


class Product(SharedBase, Base):
    """Product Table"""
    __tablename__ = 'products'

    # products must have Insertion_Order for ordering purpose
    # must be a primary key for auto increment so id must be overrided
    insertion_order = Column(Integer, autoincrement=True, primary_key=True)
    
    # override id and remove primary key constraint
    id = Column(String(128), unique=True)

    title = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(1024), nullable=False)
    discount = Column(Integer, CheckConstraint('discount <= 100'), default=0)
    category_name = Column(String(127), nullable=False)
    category_type = Column(String(127), nullable=False)
    image_path = Column(String(256))
