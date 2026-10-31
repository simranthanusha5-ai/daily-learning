"""Day 349: Schnorr Zero-Knowledge Protocol."""
import random

class SchnorrZKP:
    def __init__(self, p=7919, g=7):
        self.p = p
        self.g = g

    def keygen(self, secret_x):
        public_y = pow(self.g, secret_x, self.p)
        return public_y

    def prover_commit(self, r):
        return pow(self.g, r, self.p)

    def prover_response(self, r, challenge_c, secret_x):
        return r + challenge_c * secret_x

    def verifier_verify(self, commitment_t, challenge_c, response_s, public_y):
        lhs = pow(self.g, response_s, self.p)
        rhs = (commitment_t * pow(public_y, challenge_c, self.p)) % self.p
        return lhs == rhs

if __name__ == "__main__":
    zkp = SchnorrZKP()
    x = 42 # Secret
    y = zkp.keygen(x)
    r = 17 # Ephemeral
    t = zkp.prover_commit(r)
    c = 5 # Challenge
    s = zkp.prover_response(r, c, x)
    assert zkp.verifier_verify(t, c, s, y) is True
    print("Day 349 Schnorr ZKP tests passed!")
