#!/usr/bin/python3
"""
initialize the models package
"""
from backend.data_models.stotage_engine import StorageEngine

storage = StorageEngine()
storage.reload()
