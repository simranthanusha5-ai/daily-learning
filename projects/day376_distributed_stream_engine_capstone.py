"""Day 376: Distributed Stream Processing Engine Capstone."""

class StreamMessage:
    def __init__(self, key, val, timestamp):
        self.key = key
        self.val = val
        self.timestamp = timestamp

class TumblingWindowAggregator:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.windows = {} # (key, window_start) -> sum

    def process(self, msg: StreamMessage):
        w_start = (msg.timestamp // self.window_size) * self.window_size
        k = (msg.key, w_start)
        self.windows[k] = self.windows.get(k, 0) + msg.val

class StreamEngineCapstone:
    def __init__(self):
        self.aggregator = TumblingWindowAggregator(10)
        self.checkpoints = []

    def ingest(self, msg):
        self.aggregator.process(msg)

    def trigger_checkpoint(self, checkpoint_id):
        # Save consistent snapshot of state
        snapshot = dict(self.aggregator.windows)
        self.checkpoints.append((checkpoint_id, snapshot))

if __name__ == "__main__":
    engine = StreamEngineCapstone()
    engine.ingest(StreamMessage("sensor1", 5, timestamp=2))
    engine.ingest(StreamMessage("sensor1", 10, timestamp=8))
    engine.ingest(StreamMessage("sensor1", 20, timestamp=15)) # Next window
    engine.trigger_checkpoint(1)

    assert engine.aggregator.windows[("sensor1", 0)] == 15
    assert engine.aggregator.windows[("sensor1", 10)] == 20
    assert len(engine.checkpoints) == 1
    print("Day 376 Capstone Stream Engine tests passed!")
