#!/usr/bin/python3
""" Order_item model"""
from backend.models.shared import SharedBase, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class OrderItem(SharedBase, Base):
    """Order_items table"""
    __tablename__ = 'order_items'
    item_quantity = Column(Integer, default=1)
    product_id = Column(String(128), ForeignKey('products.id'), nullable=False)
    order_id = Column(String(128), ForeignKey('orders.id'), nullable=False)
