"""Day 326: Epoll Edge vs Level Triggered."""

class EpollSimulator:
    def __init__(self):
        self.buffers = {} # fd -> bytes
        self.watches = {} # fd -> is_edge_triggered
        self.last_state = {} # fd -> has_data

    def register(self, fd, edge_triggered=False):
        self.watches[fd] = edge_triggered
        self.buffers[fd] = bytearray()
        self.last_state[fd] = False

    def write_data(self, fd, data):
        self.buffers[fd].extend(data)

    def poll(self):
        events = []
        for fd, et in self.watches.items():
            has_data = len(self.buffers[fd]) > 0
            if et:
                # Trigger only on transition False -> True
                if has_data and not self.last_state[fd]:
                    events.append(fd)
            else:
                if has_data:
                    events.append(fd)
            self.last_state[fd] = has_data
        return events

if __name__ == "__main__":
    ep = EpollSimulator()
    ep.register(1, edge_triggered=True)
    ep.register(2, edge_triggered=False)
    ep.write_data(1, b"abc")
    ep.write_data(2, b"xyz")
    assert ep.poll() == [1, 2]
    # In next poll, edge-triggered 1 won't refire unless new data arrives
    assert ep.poll() == [2]
    print("Day 326 Epoll Semantics tests passed!")
