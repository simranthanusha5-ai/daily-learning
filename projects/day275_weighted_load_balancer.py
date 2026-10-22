"""Day 275: Weighted Least-Connections Load Balancer."""

class BackendServer:
    def __init__(self, name, weight=1):
        self.name = name
        self.weight = weight
        self.active_conns = 0

class WeightedLB:
    def __init__(self, servers):
        self.servers = servers

    def select(self):
        # Best server has smallest active_conns / weight ratio
        best = min(self.servers, key=lambda s: s.active_conns / s.weight)
        best.active_conns += 1
        return best

    def release(self, server):
        server.active_conns = max(0, server.active_conns - 1)

if __name__ == "__main__":
    s1 = BackendServer("srv_low", weight=1)
    s2 = BackendServer("srv_high", weight=2)
    lb = WeightedLB([s1, s2])
    c1 = lb.select()
    c2 = lb.select()
    # s2 gets assigned twice as easily due to weight 2
    assert c1.name == "srv_high" or c2.name == "srv_high"
    print("Day 275 Load Balancer tests passed!")
