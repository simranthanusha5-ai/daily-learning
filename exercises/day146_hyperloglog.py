"""Day 146: HyperLogLog Cardinality Estimator."""
import hashlib
import math

class HyperLogLog:
    def __init__(self, b=4):
        self.b = b
        self.m = 1 << b
        self.registers = [0] * self.m
        self.alpha = 0.7213 / (1 + 1.079 / self.m)

    def _hash(self, val):
        return int(hashlib.md5(str(val).encode()).hexdigest()[:8], 16)

    def add(self, val):
        x = self._hash(val)
        j = x & (self.m - 1)
        w = x >> self.b
        rho = (w ^ (w - 1)).bit_length() if w != 0 else 32
        self.registers[j] = max(self.registers[j], rho)

    def count(self):
        z = sum(2.0 ** -val for val in self.registers)
        raw_est = self.alpha * (self.m ** 2) / z
        return int(raw_est)

if __name__ == "__main__":
    hll = HyperLogLog()
    for i in range(100):
        hll.add(f"user_{i}")
    est = hll.count()
    assert est > 30 # Rough probabilistic bound
    print("Day 146 HyperLogLog tests passed!")
