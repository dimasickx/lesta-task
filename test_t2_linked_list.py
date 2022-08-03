import unittest
from t2_fifo_linked_list import QueueLinkedList


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_count(self):
        self.queue = QueueLinkedList()
        for i in range(6):
            self.queue.enqueue(i)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(self.queue.count, 4)

    def test_iteration(self):
        self.queue = QueueLinkedList()
        for i in range(10):
            self.queue.enqueue(i + 3)
        for i, v in enumerate(self.queue):
            if i == self.queue.count:
                break
            self.assertEqual(i + 3, v)

    def test_empty(self):
        self.queue = QueueLinkedList()
        with self.assertRaises(StopIteration):
            self.queue.dequeue()

    def test_fifo(self):
        self.queue = QueueLinkedList()
        self.queue.enqueue(4)
        self.queue.enqueue(9)
        self.assertEqual(self.queue.dequeue(), 4)

    def test_ring(self):
        self.queue = QueueLinkedList()
        self.queue.enqueue(9)
        self.queue.enqueue(4)
        next_after_last = self.queue.tail.next_item.value
        first = self.queue.head.value
        self.assertEqual(next_after_last, first)


if __name__ == '__main__':
    unittest.main()
