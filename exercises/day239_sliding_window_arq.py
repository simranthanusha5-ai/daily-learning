"""Day 239: Go-Back-N ARQ."""

class SenderGBN:
    def __init__(self, window_size=4):
        self.w = window_size
        self.base = 0
        self.next_seq = 0
        self.buffer = []

    def send(self, packet):
        if self.next_seq < self.base + self.w:
            self.buffer.append(packet)
            self.next_seq += 1
            return True
        return False

    def receive_ack(self, ack_num):
        if ack_num >= self.base:
            self.base = ack_num + 1

if __name__ == "__main__":
    gbn = SenderGBN(window_size=3)
    assert gbn.send("p0") is True
    assert gbn.send("p1") is True
    assert gbn.send("p2") is True
    assert gbn.send("p3") is False # Window full
    gbn.receive_ack(1)
    assert gbn.send("p3") is True # Advance window
    print("Day 239 GBN ARQ tests passed!")
