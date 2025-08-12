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
        self.assertEqual(self.calc.calculate_rpm(60, 60), 60)  # 60 miles in 60 minutes = 60 RPM
        self.assertEqual(self.calc.calculate_rpm(30, 60), 30)  # 30 miles in 60 minutes = 30 RPM
        self.assertEqual(self.calc.calculate_rpm(120, 60), 120)  # 120 miles in 60 minutes = 120 RPM
        self.assertAlmostEqual(self.calc.calculate_rpm(45, 30), 90, places=2)  # 45 miles in 30 minutes = 90 RPM

        with self.assertRaises(ValueError):
            self.calc.calculate_rpm(60, 0)  # Time cannot be zero

if __name__ == '__main__':
    unittest.main()