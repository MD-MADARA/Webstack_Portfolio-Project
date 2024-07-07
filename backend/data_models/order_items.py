#!/usr/bin/python3
""" Order_item model"""
from backend.data_models.shared import SharedBase, Base
from sqlalchemy import Column, Integer, ForeignKey


class OrderItem(SharedBase, Base):
    """Order_items table"""
    __tablename__ = 'order_items'
    item_quantity = Column(Integer, default=1)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
