#!/usr/bin/env python3
"""
Function that changes all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """Update the document topics based on name"""
    mongo_collection.update_many({"name": name}, {"$set": {'topics': topics}})
