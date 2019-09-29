from LinkedList import List as ls


class Queue:
    def __init__(self, item, nec_size):
        self.queue = ls()
        if nec_size < 1:
            raise ValueError("k should be >= 1")
        self.nec_size = nec_size  # k
        self.queue.append(item)

    def enqueue(self, item):
        length = self.queue.length()
        if length >= self.nec_size:
            self.queue.append_first(item)
            self.queue.pop()
        else:
            self.queue.append_first(item)

    def dequeue(self):
        if self.queue.length() - 1 <= 0:
            raise ValueError("Queue can not be empty")
        return self.queue.pop()

    def __len__(self):
        return self.queue.length()

    def __str__(self):
        return self.queue.__str__()
