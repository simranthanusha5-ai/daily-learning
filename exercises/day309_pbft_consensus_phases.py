"""Day 309: PBFT 3-Phase Consensus."""

class PBFTReplica:
    def __init__(self, rep_id, total_f):
        self.id = rep_id
        self.f = total_f
        self.pre_prepares = {}
        self.prepares = {}
        self.commits = {}
        self.committed = set()

    def receive_pre_prepare(self, view, seq, digest):
        self.pre_prepares[seq] = digest
        return ("PREPARE", view, seq, digest, self.id)

    def receive_prepare(self, seq, digest, sender):
        self.prepares.setdefault(seq, set()).add(sender)
        # 2f prepares threshold
        if len(self.prepares[seq]) >= 2 * self.f:
            return ("COMMIT", seq, digest, self.id)
        return None

    def receive_commit(self, seq, sender):
        self.commits.setdefault(seq, set()).add(sender)
        if len(self.commits[seq]) >= 2 * self.f + 1:
            self.committed.add(seq)
            return True
        return False

if __name__ == "__main__":
    rep = PBFTReplica(0, total_f=1)
    rep.receive_pre_prepare(0, 1, "h(req)")
    rep.receive_prepare(1, "h(req)", sender=1)
    rep.receive_prepare(1, "h(req)", sender=2)
    rep.receive_commit(1, sender=0)
    rep.receive_commit(1, sender=1)
    ok = rep.receive_commit(1, sender=2)
    assert ok is True
    assert 1 in rep.committed
    print("Day 309 PBFT Consensus tests passed!")
