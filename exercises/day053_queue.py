# Day 53: Queue with collections.deque
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()

    def __len__(self):
        return len(self._items)

q = Queue()
q.enqueue("Customer 1")
q.enqueue("Customer 2")
q.enqueue("Customer 3")

print("Served:", q.dequeue())
print("Remaining in line:", len(q))
