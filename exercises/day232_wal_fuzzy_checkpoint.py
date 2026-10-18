"""Day 232: WAL Checkpointing."""

class DBCheckpointEngine:
    def __init__(self):
        self.dirty_pages = {}
        self.disk_storage = {}
        self.wal_log = []

    def log_and_mutate(self, lsn, page_id, val):
        self.wal_log.append((lsn, page_id, val))
        self.dirty_pages[page_id] = val

    def checkpoint(self):
        # Flush all dirty pages to disk
        self.disk_storage.update(self.dirty_pages)
        self.dirty_pages.clear()
        # Truncate WAL
        self.wal_log.clear()

if __name__ == "__main__":
    eng = DBCheckpointEngine()
    eng.log_and_mutate(1, "page_10", "data_A")
    assert len(eng.wal_log) == 1
    eng.checkpoint()
    assert len(eng.wal_log) == 0
    assert eng.disk_storage["page_10"] == "data_A"
    print("Day 232 Checkpointing tests passed!")
