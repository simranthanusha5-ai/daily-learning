"""Day 321: POSIX Signal Delivery."""

class SignalManager:
    SIGINT = 2
    SIGTERM = 15

    def __init__(self):
        self.handlers = {}
        self.blocked_mask = set()
        self.pending_signals = []

    def register(self, sig, handler):
        self.handlers[sig] = handler

    def block(self, sig):
        self.blocked_mask.add(sig)

    def unblock(self, sig):
        self.blocked_mask.discard(sig)
        self.drain()

    def send(self, sig):
        if sig in self.blocked_mask:
            self.pending_signals.append(sig)
        elif sig in self.handlers:
            self.handlers[sig]()

    def drain(self):
        to_process = [s for s in self.pending_signals if s not in self.blocked_mask]
        self.pending_signals = [s for s in self.pending_signals if s in self.blocked_mask]
        for s in to_process:
            if s in self.handlers:
                self.handlers[s]()

if __name__ == "__main__":
    sm = SignalManager()
    log = []
    sm.register(SignalManager.SIGINT, lambda: log.append("SIGINT"))
    sm.block(SignalManager.SIGINT)
    sm.send(SignalManager.SIGINT)
    assert len(log) == 0
    sm.unblock(SignalManager.SIGINT)
    assert log == ["SIGINT"]
    print("Day 321 Signal tests passed!")
