import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_total_is_zero_on_initialization(self):
        calculator = Calculator()
        self.assertEqual(0, calculator.total())

    def test_adding_numbers(self):
        calculator = Calculator()
        calculator.add(5)
        calculator.add(10)
        self.assertEqual(15, calculator.total())

    def test_subtracting_numbers(self):
        calculator = Calculator()
        calculator.subtract(5)
        calculator.subtract(10)
        self.assertEqual(-15, calculator.total())

    def test_multiplying_numbers(self):
        calculator = Calculator()
        calculator.add(1)
        calculator.multiply(5)
        calculator.multiply(10)
        self.assertEqual(50, calculator.total())

    def test_adding_and_subtracting(self):
        calculator = Calculator()
        calculator.add(10)
        calculator.subtract(5)
        self.assertEqual(5, calculator.total())