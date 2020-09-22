import unittest

from fraction.fraction import Fraction

fraction = Fraction(1, 2)


class TestFractionClass(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(fraction), "1/2")

    def test_float(self):
        self.assertEqual(float(fraction), 0.5)
