#!/usr/bin/env python3
"""
Redis class method and a random key generator.
"""
import redis
import uuid
from typing import Union

class Cache:
    """Initialize the cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Take data argument and return a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
