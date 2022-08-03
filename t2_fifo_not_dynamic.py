class FifoCircularBuffer:
    def __init__(self, capacity):
        self.cap = capacity
        self.queue = [None for _ in range(self.cap)]
        self.write_index = -1
        self.read_index = 0

    def push(self, value):
        if (self.write_index - self.read_index) + 1 == self.cap:
            return False
        self.write_index += 1
        self.read_index = self.read_index % self.cap
        self.queue[self.write_index % self.cap] = value
        return True

    def pull(self):
        if self.write_index < self.read_index:
            return
        next_value = self.queue[self.read_index % self.cap]
        self.read_index += 1
        self.write_index = self.write_index % self.cap
        return next_value
