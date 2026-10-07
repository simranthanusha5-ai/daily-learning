"""Day 148: Snowflake ID Generator."""
import time

class SnowflakeGenerator:
    EPOCH = 1700000000000  # Custom epoch ms

    def __init__(self, worker_id, datacenter_id):
        self.worker_id = worker_id & 0x1F
        self.datacenter_id = datacenter_id & 0x1F
        self.sequence = 0
        self.last_ts = -1

    def _time_ms(self):
        return int(time.time() * 1000)

    def next_id(self):
        ts = self._time_ms()
        if ts < self.last_ts:
            raise RuntimeError("Clock moved backwards")
        if ts == self.last_ts:
            self.sequence = (self.sequence + 1) & 0xFFF
            if self.sequence == 0:
                while ts <= self.last_ts:
                    ts = self._time_ms()
        else:
            self.sequence = 0
        self.last_ts = ts

        snowflake = (((ts - self.EPOCH) << 22) |
                     (self.datacenter_id << 17) |
                     (self.worker_id << 12) |
                     self.sequence)
        return snowflake

if __name__ == "__main__":
    gen = SnowflakeGenerator(worker_id=1, datacenter_id=1)
    id1 = gen.next_id()
    id2 = gen.next_id()
    assert id1 < id2
    print("Day 148 Snowflake ID tests passed!")
