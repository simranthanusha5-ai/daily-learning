"""Day 353: Paillier Additive Homomorphic Math."""

class PaillierSystem:
    def __init__(self, p=61, q=53):
        self.n = p * q
        self.n_sq = self.n * self.n
        self.g = self.n + 1
        self.lam = (p - 1) * (q - 1)
        self.mu = pow(self.lam, -1, self.n)

    def encrypt(self, m, r=3):
        # c = g^m * r^n mod n^2
        return (pow(self.g, m, self.n_sq) * pow(r, self.n, self.n_sq)) % self.n_sq

    def decrypt(self, c):
        l = (pow(c, self.lam, self.n_sq) - 1) // self.n
        return (l * self.mu) % self.n

    def add_ciphertexts(self, c1, c2):
        return (c1 * c2) % self.n_sq

if __name__ == "__main__":
    pai = PaillierSystem()
    c1 = pai.encrypt(15, r=3)
    c2 = pai.encrypt(25, r=5)
    c_sum = pai.add_ciphertexts(c1, c2)
    assert pai.decrypt(c_sum) == 40
    print("Day 353 Paillier Homomorphic tests passed!")
