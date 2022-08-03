import unittest
from t2_fifo_not_dynamic import FifoCircularBuffer


class TestMergeSort(unittest.TestCase):
    def test_full(self):
        cb = FifoCircularBuffer(10)
        for i in range(cb.cap):
            cb.push(i + 1)
        self.assertFalse(cb.push(22))

    def test_read_get_place(self):
        cb = FifoCircularBuffer(10)
        for i in range(cb.cap):
            cb.push(i + 1)
        cb.pull()
        self.assertTrue(cb.push(33))

    def test_empty(self):
        cb = FifoCircularBuffer(1)
        self.assertIsNone(cb.pull())


if __name__ == '__main__':
    unittest.main()
