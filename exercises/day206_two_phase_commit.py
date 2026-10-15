"""Day 206: Two-Phase Commit."""

class Participant:
    def __init__(self, name, will_succeed=True):
        self.name = name
        self.will_succeed = will_succeed
        self.state = "INIT"

    def prepare(self):
        if self.will_succeed:
            self.state = "PREPARED"
            return True
        self.state = "ABORTED"
        return False

    def commit(self):
        self.state = "COMMITTED"

    def rollback(self):
        self.state = "ABORTED"

def coordinate_2pc(participants):
    votes = [p.prepare() for p in participants]
    if all(votes):
        for p in participants:
            p.commit()
        return True
    else:
        for p in participants:
            p.rollback()
        return False

if __name__ == "__main__":
    p1 = Participant("db1", True)
    p2 = Participant("db2", False)
    assert coordinate_2pc([p1, p2]) is False
    assert p1.state == "ABORTED"
    print("Day 206 2PC tests passed!")
