"""Day 208: Distributed Lock Lease."""
import time

class LockStore:
    def __init__(self):
        self.holder = None
        self.lease_expires = 0

    def acquire(self, client_id, ttl=1.0):
        now = time.time()
        if self.holder is None or now > self.lease_expires:
            self.holder = client_id
            self.lease_expires = now + ttl
            return True
        return False

    def renew(self, client_id, ttl=1.0):
        now = time.time()
        if self.holder == client_id and now <= self.lease_expires:
            self.lease_expires = now + ttl
            return True
        return False

    def release(self, client_id):
        if self.holder == client_id:
            self.holder = None
            self.lease_expires = 0

if __name__ == "__main__":
    store = LockStore()
    assert store.acquire("worker_1", ttl=0.1) is True
    assert store.acquire("worker_2", ttl=0.1) is False
    time.sleep(0.12)
    assert store.acquire("worker_2", ttl=0.1) is True
    print("Day 208 Distributed Lock tests passed!")
