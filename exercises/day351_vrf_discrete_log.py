"""Day 351: Verifiable Random Function (VRF)."""
import hashlib

class SimpleVRF:
    def __init__(self, p=7919, g=7):
        self.p = p
        self.g = g

    def evaluate(self, secret_key, message):
        h_m = int(hashlib.sha256(message.encode()).hexdigest(), 16) % self.p
        v = pow(h_m, secret_key, self.p)
        proof = (v, secret_key) # Simplified non-interactive proof tuple
        random_output = hashlib.sha256(str(v).encode()).hexdigest()
        return random_output, proof

if __name__ == "__main__":
    vrf = SimpleVRF()
    rand1, _ = vrf.evaluate(13, "seed_42")
    rand2, _ = vrf.evaluate(13, "seed_42")
    assert rand1 == rand2
    print("Day 351 VRF tests passed!")
