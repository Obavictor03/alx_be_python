import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 4), 9)
        self.assertEqual(self.calc.add(-1, 6), 5)
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 4), 1)
        self.assertEqual(self.calc.subtract(-1, 6), -7)
        self.assertEqual(self.calc.subtract(-2, -3), 1)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 4), 20)
        self.assertEqual(self.calc.multiply(-1, 6), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_division(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(0, 6), 0)
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertEqual(self.calc.divide(10, -2), -5)