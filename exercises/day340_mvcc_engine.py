"""Day 340: MVCC Storage Engine."""

class MVCCRecord:
    def __init__(self, key, val, created_by):
        self.key = key
        self.val = val
        self.created_by = created_by
        self.deleted_by = None

class MVCCStore:
    def __init__(self):
        self.versions = []
        self.tx_counter = 0

    def begin(self):
        self.tx_counter += 1
        return self.tx_counter

    def write(self, tx_id, key, val):
        self.versions.append(MVCCRecord(key, val, created_by=tx_id))

    def read(self, snapshot_tx_id, key):
        for rec in reversed(self.versions):
            if rec.key == key and rec.created_by <= snapshot_tx_id:
                if rec.deleted_by is None or rec.deleted_by > snapshot_tx_id:
                    return rec.val
        return None

if __name__ == "__main__":
    store = MVCCStore()
    t1 = store.begin()
    store.write(t1, "balance", 100)
    t2 = store.begin() # Snapshot sees balance 100
    t3 = store.begin()
    store.write(t3, "balance", 200)
    assert store.read(t2, "balance") == 100
    assert store.read(t3, "balance") == 200
    print("Day 340 MVCC tests passed!")
