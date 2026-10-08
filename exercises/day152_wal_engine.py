"""Day 152: Write-Ahead Logging (WAL) Engine."""
import json
import os

class WALEngine:
    def __init__(self, log_path):
        self.log_path = log_path
        self.state = {}
        self._recover()

    def _recover(self):
        if not os.path.exists(self.log_path):
            return
        with open(self.log_path, 'r') as f:
            for line in f:
                if line.strip():
                    entry = json.loads(line)
                    op, k, v = entry['op'], entry['k'], entry.get('v')
                    if op == 'SET':
                        self.state[k] = v
                    elif op == 'DEL' and k in self.state:
                        del self.state[k]

    def set(self, k, v):
        self._append_log({"op": "SET", "k": k, "v": v})
        self.state[k] = v

    def delete(self, k):
        self._append_log({"op": "DEL", "k": k})
        if k in self.state:
            del self.state[k]

    def _append_log(self, entry):
        with open(self.log_path, 'a') as f:
            f.write(json.dumps(entry) + "\n")
            f.flush()

if __name__ == "__main__":
    log_file = "/tmp/test_wal.log"
    if os.path.exists(log_file):
        os.remove(log_file)
    wal = WALEngine(log_file)
    wal.set("alpha", 42)
    wal.set("beta", 99)
    # Simulate crash & restart
    wal2 = WALEngine(log_file)
    assert wal2.state["alpha"] == 42
    assert wal2.state["beta"] == 99
    if os.path.exists(log_file):
        os.remove(log_file)
    print("Day 152 WAL tests passed!")
