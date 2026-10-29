"""Day 332: BGP Path Vector Routing."""

class BGPRoute:
    def __init__(self, prefix, as_path, next_hop):
        self.prefix = prefix
        self.as_path = list(as_path)
        self.next_hop = next_hop

class BGPRouter:
    def __init__(self, my_as):
        self.my_as = my_as
        self.rib = {} # prefix -> BGPRoute

    def receive_update(self, route):
        # AS-Loop detection
        if self.my_as in route.as_path:
            return False # Reject loop
        # Best path: prefer shorter AS path
        if route.prefix not in self.rib or len(route.as_path) < len(self.rib[route.prefix].as_path):
            self.rib[route.prefix] = route
            return True
        return False

if __name__ == "__main__":
    r = BGPRouter(my_as=65001)
    r1 = BGPRoute("198.51.100.0/24", [65002, 65003], "10.1.1.1")
    r2_loop = BGPRoute("198.51.100.0/24", [65004, 65001], "10.1.1.2")
    assert r.receive_update(r1) is True
    assert r.receive_update(r2_loop) is False # Loop detected
    print("Day 332 BGP tests passed!")
