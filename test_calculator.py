import unittest
from unittest.mock import MagicMock
from calculator import Calculator

class MockRedis:
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.mock_redis = MockRedis()
        self.calc = Calculator()
        self.calc.redis_client = self.mock_redis

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 4), -4)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_caching(self):
        # Test that results are cached
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        self.assertEqual(self.mock_redis.get("calc:add:2:3"), b"5.0")

        # Test that cached results are used
        self.mock_redis.get = MagicMock(return_value=b"5.0")
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        self.mock_redis.get.assert_called_once_with("calc:add:2:3")

if __name__ == '__main__':
    unittest.main()