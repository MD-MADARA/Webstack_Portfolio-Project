#!/usr/bin/python3
"""
initialize the models package
"""
from backend.models.storage_engine import StorageEngine

storage = StorageEngine()
storage.reload()
