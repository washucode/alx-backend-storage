#!/usr/bin/env python3

"""
Redis basic exercise
"""

import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Method that takes a single
    method Callable argument and returns a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Method that takes a single
    method Callable argument and returns a Callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper method
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output
    return wrapper


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

    @count_calls
    @call_history
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
