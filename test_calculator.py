import unittest
from calculator import MemoryCalculator

class TestMemoryCalculator(unittest.TestCase):

  def test_total_is_zero_on_initialization(self):
    calculator = calculator()
    self.assertEqual(0, calculator.total())

    def test_adding_numbers(self):
        calculator = MemoryCalculator()
        calculator.add(5)
        calculator.add(10)
        self.assertEqual(15, calculator.total())

    def test_subtracting_numbers(self):
        calculator = MemoryCalculator()
        calculator.subtract(5)
        calculator.subtract(10)
        self.assertEqual(-15, calculator.total())

    def test_multiplying_numbers(self):
        calculator = MemoryCalculator()
        calculator.multiply(5)
        calculator.multiply(10)
        self.assertEqual(50, calculator.total())

    def test_adding_and_subtracting(self):
        calculator = MemoryCalculator()
        calculator.add(10)
        calculator.subtract(5)
        self.assertEqual(5, calculator.total())