"""Day 241: CIDR Longest Prefix Match."""

def ip_to_int(ip_str):
    parts = [int(p) for p in ip_str.split(".")]
    return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

class RouterTable:
    def __init__(self):
        self.routes = []

    def add_route(self, cidr, next_hop):
        ip, prefix = cidr.split("/")
        mask = ((1 << int(prefix)) - 1) << (32 - int(prefix))
        self.routes.append((int(prefix), ip_to_int(ip) & mask, mask, next_hop))
        self.routes.sort(key=lambda r: r[0], reverse=True) # Longest prefix first

    def lookup(self, ip_str):
        ip_num = ip_to_int(ip_str)
        for _, net, mask, hop in self.routes:
            if (ip_num & mask) == net:
                return hop
        return "DEFAULT"

if __name__ == "__main__":
    rt = RouterTable()
    rt.add_route("192.168.0.0/16", "eth0")
    rt.add_route("192.168.1.0/24", "eth1")
    assert rt.lookup("192.168.1.55") == "eth1"
    assert rt.lookup("192.168.2.10") == "eth0"
    print("Day 241 CIDR LPM Router tests passed!")
