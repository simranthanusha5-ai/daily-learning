"""Day 341: ARIES Crash Recovery."""

class ARIESRecovery:
    def __init__(self):
        self.wal = []

    def log(self, lsn, tx_id, op, k, v, prev_lsn=None):
        self.wal.append({"lsn": lsn, "tx": tx_id, "op": op, "k": k, "v": v, "prev": prev_lsn})

    def recover(self):
        # 1. Analysis Phase
        active_txs = set()
        for e in self.wal:
            if e["op"] == "COMMIT": active_txs.discard(e["tx"])
            else: active_txs.add(e["tx"])
        # 2. Redo Phase
        db = {}
        for e in self.wal:
            if e["op"] == "SET": db[e["k"]] = e["v"]
        # 3. Undo Phase: Rollback uncommitted transactions
        for e in reversed(self.wal):
            if e["tx"] in active_txs and e["op"] == "SET":
                db.pop(e["k"], None)
        return db

if __name__ == "__main__":
    aries = ARIESRecovery()
    aries.log(1, "T1", "SET", "x", 10)
    aries.log(2, "T1", "COMMIT", None, None)
    aries.log(3, "T2", "SET", "y", 20) # T2 uncommitted at crash
    state = aries.recover()
    assert state.get("x") == 10
    assert "y" not in state
    print("Day 341 ARIES Recovery tests passed!")
