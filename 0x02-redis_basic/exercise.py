#!/usr/bin/env python3

"""
Redis basic exercise
"""

import redis
import uuid
from typing import Union, Optional, Callable, Any


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method that stores data to redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Method that gets data from redis
        """
        data = self._redis.get(key)
        if data is not None and fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Method that converts bytes to str
        """
        return self.get(key, fn=lambda x: x.decode('utf-8') if x else None)

    def get_int(self, key: str) -> Union[int, None]:
        """
        Method that converts bytes to int
        """
        return self.get(key, fn=lambda x: int(x) if x else None)
