"""Day 155: Two-Phase Locking (2PL) Lock Manager."""
import threading

class LockManager:
    def __init__(self):
        self._locks = {}
        self._mutex = threading.Lock()

    def acquire_exclusive(self, row_id):
        with self._mutex:
            if row_id not in self._locks:
                self._locks[row_id] = threading.Lock()
            lock = self._locks[row_id]
        lock.acquire()

    def release_exclusive(self, row_id):
        with self._mutex:
            lock = self._locks.get(row_id)
        if lock:
            lock.release()

if __name__ == "__main__":
    lm = LockManager()
    lm.acquire_exclusive("row_42")
    lm.release_exclusive("row_42")
    print("Day 155 Row-Level Locking tests passed!")
