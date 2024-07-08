#!/usr/bin/python3
"""
initialize the models package
"""
from backend.data_models.storage_engine import StorageEngine

storage = StorageEngine()
storage.reload()
