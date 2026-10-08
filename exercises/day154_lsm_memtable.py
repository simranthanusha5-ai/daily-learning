"""Day 154: LSM Memtable Architecture."""

class MemTable:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.data = {}
        self.flushed_sstables = []

    def put(self, key, value):
        self.data[key] = value
        if len(self.data) >= self.capacity:
            self._flush()

    def _flush(self):
        sorted_pairs = sorted(self.data.items())
        self.flushed_sstables.append(sorted_pairs)
        self.data = {}

    def get(self, key):
        if key in self.data:
            return self.data[key]
        for sstable in reversed(self.flushed_sstables):
            for k, v in sstable:
                if k == key:
                    return v
        return None

if __name__ == "__main__":
    mem = MemTable(capacity=2)
    mem.put("k1", "v1")
    mem.put("k2", "v2")
    assert len(mem.flushed_sstables) == 1
    assert mem.get("k1") == "v1"
    print("Day 154 LSM Memtable tests passed!")
