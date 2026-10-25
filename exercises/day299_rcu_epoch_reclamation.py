"""Day 299: RCU Epoch-Based Reclamation."""

class RCUStore:
    def __init__(self):
        self.epoch = 0
        self.active_readers = {0: 0, 1: 0}
        self.data = {"key": "v1"}
        self.retired_objects = []

    def rcu_read_lock(self):
        e = self.epoch
        self.active_readers[e] += 1
        return e

    def rcu_read_unlock(self, epoch):
        self.active_readers[epoch] -= 1

    def update(self, key, val):
        old_data = self.data
        # Copy and update
        new_data = dict(old_data)
        new_data[key] = val
        self.data = new_data
        self.retired_objects.append((self.epoch, old_data))

    def synchronize_rcu(self):
        # Advance epoch
        prev_epoch = self.epoch
        self.epoch ^= 1
        # Reclaim only after readers on prev_epoch finish
        if self.active_readers[prev_epoch] == 0:
            self.retired_objects = [(e, obj) for e, obj in self.retired_objects if e != prev_epoch]

if __name__ == "__main__":
    rcu = RCUStore()
    reader_e = rcu.rcu_read_lock()
    rcu.update("key", "v2")
    assert rcu.data["key"] == "v2"
    rcu.rcu_read_unlock(reader_e)
    rcu.synchronize_rcu()
    assert len(rcu.retired_objects) == 0
    print("Day 299 RCU Reclamation tests passed!")
