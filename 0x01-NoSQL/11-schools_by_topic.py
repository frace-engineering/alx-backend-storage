#!/usr/bin/env python3
"""
 Function that returns the list of school having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """Return list of schools having topic."""
    if mongo_collection is None or topic is None:
        return [{}]
    return list(mongo_collection.find({"topic": topic}))
