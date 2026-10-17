"""Day 226: Merkle-Hellman Knapsack."""

class MerkleHellman:
    def __init__(self):
        # Superincreasing private key
        self.w = [2, 7, 11, 21, 42, 89, 180, 354]
        self.q = 881
        self.r = 588
        self.r_inv = pow(self.r, -1, self.q)
        # Public key
        self.beta = [(x * self.r) % self.q for x in self.w]

    def encrypt(self, bit_list):
        return sum(b * pub for b, pub in zip(bit_list, self.beta))

    def decrypt(self, ciphertext):
        c_prime = (ciphertext * self.r_inv) % self.q
        bits = [0] * len(self.w)
        for i in reversed(range(len(self.w))):
            if self.w[i] <= c_prime:
                bits[i] = 1
                c_prime -= self.w[i]
        return bits

if __name__ == "__main__":
    mh = MerkleHellman()
    msg = [1, 0, 1, 1, 0, 0, 1, 0]
    cipher = mh.encrypt(msg)
    plain = mh.decrypt(cipher)
    assert plain == msg
    print("Day 226 Knapsack Cryptosystem tests passed!")
