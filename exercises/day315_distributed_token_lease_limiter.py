"""Day 315: Distributed Token Lease Limiter."""

class CentralTokenAuthority:
    def __init__(self, total_tokens=1000):
        self.remaining = total_tokens

    def request_batch(self, count):
        granted = min(self.remaining, count)
        self.remaining -= granted
        return granted

class LocalTokenLease:
    def __init__(self, authority, batch_size=50):
        self.authority = authority
        self.batch_size = batch_size
        self.local_tokens = 0

    def consume(self):
        if self.local_tokens == 0:
            self.local_tokens = self.authority.request_batch(self.batch_size)
        if self.local_tokens > 0:
            self.local_tokens -= 1
            return True
        return False

if __name__ == "__main__":
    auth = CentralTokenAuthority(100)
    client = LocalTokenLease(auth, batch_size=20)
    assert client.consume() is True
    assert client.local_tokens == 19
    assert auth.remaining == 80
    print("Day 315 Token Lease Limiter tests passed!")
