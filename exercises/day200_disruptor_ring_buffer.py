"""Day 200: Disruptor Ring Buffer."""

class RingBuffer:
    def __init__(self, capacity=16):
        assert (capacity & (capacity - 1)) == 0, "Capacity must be power of 2"
        self.capacity = capacity
        self.mask = capacity - 1
        self.buffer = [None] * capacity
        self.cursor = -1

    def claim(self):
        self.cursor += 1
        return self.cursor

    def publish(self, seq, data):
        self.buffer[seq & self.mask] = data

    def get(self, seq):
        return self.buffer[seq & self.mask]

if __name__ == "__main__":
    rb = RingBuffer(8)
    seq = rb.claim()
    rb.publish(seq, "event_0")
    assert rb.get(seq) == "event_0"
    print("Day 200 Disruptor Ring Buffer tests passed!")
