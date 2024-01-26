import pytest
from exercise import Cache


def test_cache():
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    # Additional test cases for get_str and get_int methods
    str_key = cache.store("Hello, World!")
    int_key = cache.store(42)

    assert cache.get_str(str_key) == "Hello, World!"
    assert cache.get_int(int_key) == 42


if __name__ == "__main__":
    pytest.main(["-v", "1-main.py"])
