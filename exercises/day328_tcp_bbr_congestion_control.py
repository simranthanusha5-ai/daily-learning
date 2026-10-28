"""Day 328: TCP BBR Congestion Control."""

class BBRController:
    STARTUP = 0
    DRAIN = 1
    PROBE_BW = 2
    PROBE_RTT = 3

    def __init__(self):
        self.state = self.STARTUP
        self.min_rtt = float('inf')
        self.max_bw = 0.0

    def on_ack(self, delivery_rate, rtt):
        self.min_rtt = min(self.min_rtt, rtt)
        self.max_bw = max(self.max_bw, delivery_rate)
        if self.state == self.STARTUP and delivery_rate < self.max_bw * 1.1:
            self.state = self.DRAIN
        elif self.state == self.DRAIN:
            self.state = self.PROBE_BW

    def pacing_rate(self):
        gain = 2.88 if self.state == self.STARTUP else 1.0
        return self.max_bw * gain

if __name__ == "__main__":
    bbr = BBRController()
    bbr.on_ack(delivery_rate=100.0, rtt=0.02)
    bbr.on_ack(delivery_rate=105.0, rtt=0.02)
    assert bbr.state in [BBRController.DRAIN, BBRController.PROBE_BW]
    print("Day 328 BBR tests passed!")
