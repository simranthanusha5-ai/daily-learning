"""Day 300: LMAX Disruptor Pipeline."""

class DisruptorPipeline:
    def __init__(self, size=8):
        self.ring = [None] * size
        self.mask = size - 1
        self.producer_cursor = -1
        self.c1_cursor = -1
        self.c2_cursor = -1

    def publish(self, event):
        self.producer_cursor += 1
        self.ring[self.producer_cursor & self.mask] = event

    def step_c1(self, handler):
        while self.c1_cursor < self.producer_cursor:
            self.c1_cursor += 1
            handler(self.ring[self.c1_cursor & self.mask])

    def step_c2(self, handler):
        # c2 depends on c1
        while self.c2_cursor < self.c1_cursor:
            self.c2_cursor += 1
            handler(self.ring[self.c2_cursor & self.mask])

if __name__ == "__main__":
    p = DisruptorPipeline(4)
    log1, log2 = [], []
    p.publish("trade_1")
    p.step_c1(lambda e: log1.append(f"audited:{e}"))
    p.step_c2(lambda e: log2.append(f"journaled:{e}"))
    assert log1 == ["audited:trade_1"]
    assert log2 == ["journaled:trade_1"]
    print("Day 300 Disruptor Multi-Consumer tests passed!")
