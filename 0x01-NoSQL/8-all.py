#!/usr/bin/env python3
"""
Python function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """List the documents withing the collection"""
    return list(mongo_collection.find())
