"""Day 199: Lock-free Stack simulation."""
import threading

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LockFreeStack:
    def __init__(self):
        self.head = None
        self._lock = threading.Lock() # Simulates hardware CAS

    def _cas(self, old_head, new_head):
        with self._lock:
            if self.head == old_head:
                self.head = new_head
                return True
            return False

    def push(self, val):
        node = Node(val)
        while True:
            old_head = self.head
            node.next = old_head
            if self._cas(old_head, node):
                break

    def pop(self):
        while True:
            old_head = self.head
            if not old_head:
                return None
            new_head = old_head.next
            if self._cas(old_head, new_head):
                return old_head.val

if __name__ == "__main__":
    s = LockFreeStack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() is None
    print("Day 199 Lock-Free Stack tests passed!")
