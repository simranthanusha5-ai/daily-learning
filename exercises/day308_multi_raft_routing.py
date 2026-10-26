"""Day 308: Multi-Raft Range Router."""

class MultiRaftRouter:
    def __init__(self):
        # Ranges: (start_key, end_key) -> raft_group_id
        self.ranges = [
            ("a", "m", "raft_group_1"),
            ("m", "z", "raft_group_2")
        ]
        self.groups = {
            "raft_group_1": {},
            "raft_group_2": {}
        }

    def route_key(self, key):
        for start, end, gid in self.ranges:
            if start <= key < end or (key == end and end == "z"):
                return gid
        return "raft_group_2"

    def put(self, key, val):
        gid = self.route_key(key)
        self.groups[gid][key] = val

    def get(self, key):
        gid = self.route_key(key)
        return self.groups[gid].get(key)

if __name__ == "__main__":
    router = MultiRaftRouter()
    router.put("apple", 100)
    router.put("zebra", 200)
    assert router.get("apple") == 100
    assert "apple" in router.groups["raft_group_1"]
    assert "zebra" in router.groups["raft_group_2"]
    print("Day 308 Multi-Raft Routing tests passed!")
