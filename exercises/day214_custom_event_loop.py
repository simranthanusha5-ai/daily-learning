"""Day 214: Custom Event Loop."""
from collections import deque
import time

class MiniEventLoop:
    def __init__(self):
        self.ready_queue = deque()
        self.scheduled = []

    def call_soon(self, callback, *args):
        self.ready_queue.append((callback, args))

    def run_until_complete(self):
        while self.ready_queue:
            cb, args = self.ready_queue.popleft()
            cb(*args)

if __name__ == "__main__":
    loop = MiniEventLoop()
    events = []
    loop.call_soon(lambda: events.append(1))
    loop.call_soon(lambda: events.append(2))
    loop.run_until_complete()
    assert events == [1, 2]
    print("Day 214 Custom Event Loop tests passed!")
