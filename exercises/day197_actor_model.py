"""Day 197: Actor Model."""
from queue import Queue
import threading

class Actor:
    def __init__(self):
        self._mailbox = Queue()
        self._stopped = False
        self._thread = threading.Thread(target=self._run)
        self._thread.daemon = True
        self._thread.start()

    def send(self, msg):
        self._mailbox.put(msg)

    def stop(self):
        self._stopped = True
        self._mailbox.put(None)
        self._thread.join()

    def _run(self):
        while not self._stopped:
            msg = self._mailbox.get()
            if msg is None:
                break
            self.receive(msg)

    def receive(self, msg):
        pass

class CounterActor(Actor):
    def __init__(self):
        self.count = 0
        super().__init__()

    def receive(self, msg):
        if msg == "INC":
            self.count += 1

if __name__ == "__main__":
    counter = CounterActor()
    counter.send("INC")
    counter.send("INC")
    counter.stop()
    assert counter.count == 2
    print("Day 197 Actor Model tests passed!")
