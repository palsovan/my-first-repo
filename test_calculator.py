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

    def test_pounds_to_kg(self):
        self.assertAlmostEqual(self.calc.pounds_to_kg(1), 0.45359237, places=8)
        self.assertAlmostEqual(self.calc.pounds_to_kg(10), 4.5359237, places=7)
        self.assertAlmostEqual(self.calc.pounds_to_kg(100), 45.359237, places=6)
        self.assertEqual(self.calc.pounds_to_kg(0), 0)

if __name__ == '__main__':
    unittest.main()