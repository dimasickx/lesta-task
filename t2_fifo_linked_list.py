from QueueItem import QueueItem


class QueueLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.current_item = None
        self.tail = None

    def __iter__(self):
        return self

    def next(self):
        next_item = self.current_item
        self.current_item = self.current_item.next_item
        return next_item.value

    def enqueue(self, value):
        self.count += 1
        if self.head is None:
            self.head = QueueItem(value)
            self.current_item = self.head
            self.tail = self.head
        else:
            self.current_item = self.head
            new_item = QueueItem(value, self.head)
            self.tail.next_item = new_item
            self.tail = new_item

    def dequeue(self):
        if self.head is None:
            raise StopIteration
        self.count -= 1
        result = self.head.value
        self.head = self.head.next_item
        self.current_item = self.head
        self.tail.next_item = self.head  #
        if self.head is None:
            self.tail = None
        return result


