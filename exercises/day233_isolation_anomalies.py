"""Day 233: SQL Isolation Anomalies Simulation."""

class TableStore:
    def __init__(self):
        self.rows = {"u1": 100, "u2": 200}

    def read_uncommitted(self, uncommitted_changes, key):
        return uncommitted_changes.get(key, self.rows.get(key))

    def read_committed(self, key):
        return self.rows.get(key)

if __name__ == "__main__":
    ts = TableStore()
    tx_uncommitted = {"u1": 999} # Dirty write
    # Dirty read sees 999
    assert ts.read_uncommitted(tx_uncommitted, "u1") == 999
    # Committed read sees 100
    assert ts.read_committed("u1") == 100
    print("Day 233 Isolation Anomalies tests passed!")
