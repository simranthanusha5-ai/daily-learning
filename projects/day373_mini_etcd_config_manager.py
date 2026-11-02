"""Day 373: Mini etcd Configuration Store."""

class MiniEtcd:
    def __init__(self):
        self.store = {}
        self.watchers = {}

    def put(self, key, val):
        self.store[key] = val
        for prefix, callback in self.watchers.items():
            if key.startswith(prefix):
                callback(key, val)

    def cas(self, key, old_val, new_val):
        if self.store.get(key) == old_val:
            self.put(key, new_val)
            return True
        return False

    def watch(self, prefix, callback):
        self.watchers[prefix] = callback

if __name__ == "__main__":
    etcd = MiniEtcd()
    events = []
    etcd.watch("/config/", lambda k, v: events.append((k, v)))
    etcd.put("/config/db_host", "localhost")
    assert etcd.cas("/config/db_host", "localhost", "127.0.0.1") is True
    assert len(events) == 2
    print("Day 373 Mini etcd tests passed!")
