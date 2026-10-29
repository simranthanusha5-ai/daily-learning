"""Day 333: NAT Translation Simulator."""

class SymmetricNAT:
    def __init__(self, public_ip):
        self.public_ip = public_ip
        self.mappings = {} # (internal_ip, internal_port, remote_ip, remote_port) -> mapped_port
        self.next_port = 10000

    def outbound(self, src_ip, src_port, dst_ip, dst_port):
        key = (src_ip, src_port, dst_ip, dst_port)
        if key not in self.mappings:
            self.mappings[key] = self.next_port
            self.next_port += 1
        return (self.public_ip, self.mappings[key])

if __name__ == "__main__":
    nat = SymmetricNAT("203.0.113.1")
    p1 = nat.outbound("192.168.1.10", 5000, "1.1.1.1", 80)
    p2 = nat.outbound("192.168.1.10", 5000, "8.8.8.8", 80)
    # Symmetric NAT allocates distinct ports for different destinations
    assert p1[1] != p2[1]
    print("Day 333 NAT tests passed!")
