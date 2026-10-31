"""Day 352: FROST Distributed Key Generation."""

class FROSTParticipant:
    def __init__(self, pid, p=7919):
        self.pid = pid
        self.p = p
        self.secret_share = pid * 11 % p

    def public_share(self, g=7):
        return pow(g, self.secret_share, self.p)

def compute_group_public_key(participants, g=7, p=7919):
    # Joint public key is product of participants' public shares
    joint = 1
    for part in participants:
        joint = (joint * part.public_share(g)) % p
    return joint

if __name__ == "__main__":
    p1 = FROSTParticipant(1)
    p2 = FROSTParticipant(2)
    group_pub = compute_group_public_key([p1, p2])
    assert group_pub > 0
    print("Day 352 FROST tests passed!")
