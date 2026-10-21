"""Day 260: Event Sourcing Engine."""

class BankAccountAggregate:
    def __init__(self):
        self.balance = 0
        self.events = []

    def apply(self, event):
        etype, amount = event
        if etype == "DEPOSIT":
            self.balance += amount
        elif etype == "WITHDRAW":
            self.balance -= amount
        self.events.append(event)

    def replay(self, event_stream):
        for e in event_stream:
            self.apply(e)

if __name__ == "__main__":
    acc = BankAccountAggregate()
    acc.replay([("DEPOSIT", 200), ("WITHDRAW", 50), ("DEPOSIT", 25)])
    assert acc.balance == 175
    print("Day 260 Event Sourcing tests passed!")
