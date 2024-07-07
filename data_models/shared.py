#!/usr/bin/python3
"""This module defines a shared class for all models"""
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SharedBase:
    """A base class for all models"""

    id = Column(Integer, primary_key=True, autoincrement=True)

    created_date = Column(DateTime, default=datetime.now(), nullable=False)

    updated_date = Column(DateTime, default=datetime.now(), nullable=False)

