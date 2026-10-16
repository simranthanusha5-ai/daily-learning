"""Day 209: Chandy-Lamport Snapshot."""

class Process:
    def __init__(self, pid, balance):
        self.pid = pid
        self.balance = balance
        self.saved_state = None
        self.is_recording = False

    def take_snapshot(self):
        self.saved_state = self.balance
        self.is_recording = True

    def receive_marker(self):
        if not self.is_recording:
            self.take_snapshot()

if __name__ == "__main__":
    p1 = Process(1, 100)
    p2 = Process(2, 200)
    p1.take_snapshot()
    p2.receive_marker()
    assert p1.saved_state == 100
    assert p2.saved_state == 200
    print("Day 209 Chandy-Lamport tests passed!")
