import sys
import unittest
from t3_merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negative_int(self):
        self.assertEqual(merge_sort([-5, 2, -1, -2, 0, 5, 7]), [-5, -2, -1, 0, 2, 5, 7])

    def test_one_element(self):
        self.assertEqual(merge_sort([7]), [7])

    def test_odd_len(self):
        self.assertEqual(merge_sort([7, 2, 8]), [2, 7, 8])

    def test_even_len(self):
        self.assertEqual(merge_sort([9, 3]), [3, 9])

    def test_empty(self):
        self.assertEqual(merge_sort([]), [])

    def test_none(self):
        self.assertEqual(merge_sort(None), None)

    def test_zeros(self):
        self.assertEqual(merge_sort([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_first_last_zeros(self):
        self.assertEqual(merge_sort([0, 3, 12, 0]), [0, 0, 3, 12])

    def test_duplicates(self):
        self.assertEqual(merge_sort([1, 2, 1, 2, 1, 2]), [1, 1, 1, 2, 2, 2])

    def test_max_numbers(self):
        self.assertEqual(merge_sort([sys.maxint, -22, 31, -sys.maxint - 1]), [-sys.maxint - 1, -22, 31, sys.maxint])


if __name__ == '__main__':
    unittest.main()
