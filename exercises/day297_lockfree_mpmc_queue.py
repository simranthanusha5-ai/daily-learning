"""Day 297: Lock-Free MPMC Bounded Queue."""

class Cell:
    def __init__(self, seq):
        self.seq = seq
        self.val = None

class LockFreeMPMC:
    def __init__(self, capacity=8):
        assert (capacity & (capacity - 1)) == 0
        self.cap = capacity
        self.mask = capacity - 1
        self.buffer = [Cell(i) for i in range(capacity)]
        self.enqueue_pos = 0
        self.dequeue_pos = 0

    def push(self, val):
        pos = self.enqueue_pos
        cell = self.buffer[pos & self.mask]
        if cell.seq == pos:
            self.enqueue_pos += 1
            cell.val = val
            cell.seq = pos + 1
            return True
        return False

    def pop(self):
        pos = self.dequeue_pos
        cell = self.buffer[pos & self.mask]
        if cell.seq == pos + 1:
            self.dequeue_pos += 1
            res = cell.val
            cell.seq = pos + self.mask + 1
            return res
        return None

if __name__ == "__main__":
    q = LockFreeMPMC(4)
    assert q.push("job1") is True
    assert q.push("job2") is True
    assert q.pop() == "job1"
    assert q.pop() == "job2"
    assert q.pop() is None
    print("Day 297 MPMC Queue tests passed!")
