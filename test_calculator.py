import unittest
from unittest.mock import patch
from io import StringIO
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @patch('calculator.log_info')
    def test_add(self, mock_log_info):
        self.assertEqual(self.calc.add(2, 3), 5)
        mock_log_info.assert_called_with("Addition: 2 + 3 = 5")
        
        self.assertEqual(self.calc.add(-1, 1), 0)
        mock_log_info.assert_called_with("Addition: -1 + 1 = 0")
        
        self.assertEqual(self.calc.add(-1, -1), -2)
        mock_log_info.assert_called_with("Addition: -1 + -1 = -2")

    @patch('calculator.log_info')
    def test_subtract(self, mock_log_info):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        mock_log_info.assert_called_with("Subtraction: 5 - 3 = 2")
        
        self.assertEqual(self.calc.subtract(1, 2), -1)
        mock_log_info.assert_called_with("Subtraction: 1 - 2 = -1")
        
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        mock_log_info.assert_called_with("Subtraction: -1 - -1 = 0")

    @patch('calculator.log_info')
    def test_multiply(self, mock_log_info):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        mock_log_info.assert_called_with("Multiplication: 2 * 3 = 6")
        
        self.assertEqual(self.calc.multiply(-1, 4), -4)
        mock_log_info.assert_called_with("Multiplication: -1 * 4 = -4")
        
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        mock_log_info.assert_called_with("Multiplication: -2 * -3 = 6")

    @patch('calculator.log_info')
    @patch('calculator.log_error')
    def test_divide(self, mock_log_error, mock_log_info):
        self.assertEqual(self.calc.divide(6, 3), 2)
        mock_log_info.assert_called_with("Division: 6 / 3 = 2.0")
        
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        mock_log_info.assert_called_with("Division: 7 / 2 = 3.5")
        
        self.assertEqual(self.calc.divide(-6, 2), -3)
        mock_log_info.assert_called_with("Division: -6 / 2 = -3.0")
        
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
        mock_log_error.assert_called_with("Division by zero attempted")

    @patch('calculator.log_info')
    @patch('calculator.log_warning')
    @patch('calculator.log_error')
    def test_main_function(self, mock_log_error, mock_log_warning, mock_log_info):
        with patch('builtins.input', side_effect=['add', '2', '3', 'invalid', 'subtract', '5', '3', 'quit']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                import calculator
                calculator.main()

        mock_log_info.assert_any_call("Calculator App started")
        mock_log_info.assert_any_call("Addition: 2.0 + 3.0 = 5.0")
        mock_log_warning.assert_called_with("Invalid operation attempted: invalid")
        mock_log_info.assert_any_call("Subtraction: 5.0 - 3.0 = 2.0")
        mock_log_info.assert_any_call("Calculator App finished")

if __name__ == '__main__':
    unittest.main()