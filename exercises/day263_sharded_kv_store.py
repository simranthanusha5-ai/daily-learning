"""Day 263: Sharded Key-Value Store."""
import hashlib

class ShardedKV:
    def __init__(self, num_shards=4):
        self.num_shards = num_shards
        self.shards = [{} for _ in range(num_shards)]

    def _shard_id(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16) % self.num_shards

    def put(self, key, val):
        sid = self._shard_id(key)
        self.shards[sid][key] = val

    def get(self, key):
        sid = self._shard_id(key)
        return self.shards[sid].get(key)

if __name__ == "__main__":
    kv = ShardedKV(4)
    kv.put("user_1", "Alice")
    assert kv.get("user_1") == "Alice"
    print("Day 263 Sharded KV tests passed!")
