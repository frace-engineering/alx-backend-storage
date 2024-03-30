#1/usr/bin/env python3
"""
Redis class method and a random key generator
"""
import redis
import uuid
from typing import Callable, Union


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:

        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, int)


 @functools.wraps
    def count_calls(method: Callable):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self.redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Take data argument and return a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

