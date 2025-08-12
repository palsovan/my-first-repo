import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

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

    def test_calculate_rpm(self):
        # Test normal case
        self.assertAlmostEqual(self.calc.calculate_rpm(60, 60), 60.0)
        self.assertAlmostEqual(self.calc.calculate_rpm(30, 45), 40.0)

        # Test edge cases
        self.assertAlmostEqual(self.calc.calculate_rpm(0, 60), 0.0)
        self.assertAlmostEqual(self.calc.calculate_rpm(1, 1), 60.0)

        # Test error case
        with self.assertRaises(ValueError):
            self.calc.calculate_rpm(60, 0)

if __name__ == '__main__':
    unittest.main()