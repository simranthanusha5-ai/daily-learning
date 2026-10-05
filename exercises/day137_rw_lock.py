"""Day 137: Reader-Writer Lock."""
import threading

class ReadWriteLock:
    def __init__(self):
        self._readers = 0
        self._writers_waiting = 0
        self._writing = False
        self._lock = threading.Lock()
        self._ok_to_read = threading.Condition(self._lock)
        self._ok_to_write = threading.Condition(self._lock)

    def acquire_read(self):
        with self._lock:
            while self._writing or self._writers_waiting > 0:
                self._ok_to_read.wait()
            self._readers += 1

    def release_read(self):
        with self._lock:
            self._readers -= 1
            if self._readers == 0:
                self._ok_to_write.notify()

    def acquire_write(self):
        with self._lock:
            self._writers_waiting += 1
            while self._writing or self._readers > 0:
                self._ok_to_write.wait()
            self._writers_waiting -= 1
            self._writing = True

    def release_write(self):
        with self._lock:
            self._writing = False
            if self._writers_waiting > 0:
                self._ok_to_write.notify()
            else:
                self._ok_to_read.notify_all()

if __name__ == "__main__":
    rw = ReadWriteLock()
    rw.acquire_read()
    rw.acquire_read()
    rw.release_read()
    rw.release_read()
    rw.acquire_write()
    rw.release_write()
    print("Day 137 RWLock tests passed!")
