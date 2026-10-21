"""Day 262: Round-Robin Reverse Proxy."""

class ReverseProxy:
    def __init__(self, backends):
        self.backends = [{"url": b, "healthy": True} for b in backends]
        self.idx = 0

    def mark_unhealthy(self, url):
        for b in self.backends:
            if b["url"] == url:
                b["healthy"] = False

    def route(self):
        healthy = [b for b in self.backends if b["healthy"]]
        if not healthy:
            return None
        target = healthy[self.idx % len(healthy)]
        self.idx += 1
        return target["url"]

if __name__ == "__main__":
    proxy = ReverseProxy(["b1", "b2", "b3"])
    assert proxy.route() == "b1"
    proxy.mark_unhealthy("b2")
    assert proxy.route() == "b3"
    assert proxy.route() == "b1"
    print("Day 262 Reverse Proxy tests passed!")
