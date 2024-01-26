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
