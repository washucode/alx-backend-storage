#!/usr/bin/env python3

"""
Redis basic exercise
"""

import redis
import uuid


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

    def store(self, data: bytes) -> str:
        """
        Method that generates a random key and stores the input data in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str) -> bytes:
        """
        Method that gets the data from Redis
        """
        data = self._redis.get(key)
        return data

    def get_str(self, key: str) -> str:
        """
        Method that gets the data from Redis
        """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        Method that gets the data from Redis
        """
        data = self._redis.get(key)
        return int(data)
