#!/usr/bin/env python3
""" 
Function that inserts a new document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """Retrive the _id of the inserted document"""
    return mongo_collection.insert_one(kwargs).inserted_id
