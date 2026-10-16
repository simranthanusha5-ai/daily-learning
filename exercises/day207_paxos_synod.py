"""Day 207: Single-Decree Paxos."""

class Acceptor:
    def __init__(self, id):
        self.id = id
        self.promised_id = -1
        self.accepted_id = -1
        self.accepted_val = None

    def prepare(self, prop_id):
        if prop_id > self.promised_id:
            self.promised_id = prop_id
            return True, self.accepted_id, self.accepted_val
        return False, None, None

    def accept(self, prop_id, val):
        if prop_id >= self.promised_id:
            self.promised_id = prop_id
            self.accepted_id = prop_id
            self.accepted_val = val
            return True
        return False

def run_paxos(acceptors, prop_id, prop_val):
    promises = [a.prepare(prop_id) for a in acceptors]
    ok_promises = [p for p in promises if p[0]]
    if len(ok_promises) <= len(acceptors) // 2:
        return False
    highest_id = -1
    chosen_val = prop_val
    for _, aid, aval in ok_promises:
        if aid > highest_id and aval is not None:
            highest_id = aid
            chosen_val = aval
    accepts = [a.accept(prop_id, chosen_val) for a in acceptors]
    return accepts.count(True) > len(acceptors) // 2

if __name__ == "__main__":
    accs = [Acceptor(i) for i in range(3)]
    assert run_paxos(accs, 1, "VALUE_A") is True
    print("Day 207 Paxos tests passed!")
