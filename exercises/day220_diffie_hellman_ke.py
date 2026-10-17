"""Day 220: Diffie-Hellman Key Exchange."""

def dh_generate_public(g, private_key, p):
    return pow(g, private_key, p)

def dh_compute_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)

if __name__ == "__main__":
    p = 23
    g = 5
    alice_priv = 6
    bob_priv = 15
    alice_pub = dh_generate_public(g, alice_priv, p)
    bob_pub = dh_generate_public(g, bob_priv, p)
    alice_secret = dh_compute_shared_secret(bob_pub, alice_priv, p)
    bob_secret = dh_compute_shared_secret(alice_pub, bob_priv, p)
    assert alice_secret == bob_secret
    print("Day 220 Diffie-Hellman tests passed!")
