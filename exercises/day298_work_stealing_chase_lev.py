"""Day 298: Chase-Lev Work-Stealing Deque."""

class ChaseLevDeque:
    def __init__(self, capacity=16):
        self.buffer = [None] * capacity
        self.top = 0
        self.bottom = 0

    def push(self, task):
        b = self.bottom
        self.buffer[b % len(self.buffer)] = task
        self.bottom = b + 1

    def pop(self):
        b = self.bottom - 1
        self.bottom = b
        t = self.top
        if b < t:
            self.bottom = t
            return None
        task = self.buffer[b % len(self.buffer)]
        if b > t:
            return task
        # Single element race
        if self.top == t:
            self.top = t + 1
            self.bottom = t + 1
            return task
        return None

    def steal(self):
        t = self.top
        b = self.bottom
        if t < b:
            task = self.buffer[t % len(self.buffer)]
            self.top = t + 1
            return task
        return None

if __name__ == "__main__":
    dq = ChaseLevDeque(8)
    dq.push("taskA")
    dq.push("taskB")
    assert dq.steal() == "taskA"
    assert dq.pop() == "taskB"
    print("Day 298 Chase-Lev Deque tests passed!")
