import unittest
from t1 import is_even


class TestMergeSort(unittest.TestCase):
    @staticmethod
    def mod(value):
        return value % 2 == 0

    def test_odd_number(self):
        self.assertEqual(is_even(7), self.mod(7))

    def test_even_number(self):
        self.assertEqual(is_even(6), self.mod(6))

    def test_big_number(self):
        self.assertEqual(is_even(2147483647), self.mod(2147483647))
        self.assertEqual(is_even(-2147483647), self.mod(-2147483647))

    def test_negative_number(self):
        self.assertEqual(is_even(-5), self.mod(-5))
        self.assertEqual(is_even(-8), self.mod(-8))


if __name__ == '__main__':
    unittest.main()
