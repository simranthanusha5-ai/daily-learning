"""Day 331: WireGuard Cryptokey Routing."""

class WireGuardInterface:
    def __init__(self):
        self.peers = {} # pubkey -> allowed_ip

    def add_peer(self, public_key, allowed_ip):
        self.peers[public_key] = allowed_ip

    def route_inbound_packet(self, sender_pubkey, packet_dest_ip):
        # Cryptokey check: verify sender owns allowed IP
        if self.peers.get(sender_pubkey) == packet_dest_ip:
            return True
        return False

if __name__ == "__main__":
    wg = WireGuardInterface()
    wg.add_peer("pub_peer_A", "10.0.0.2")
    assert wg.route_inbound_packet("pub_peer_A", "10.0.0.2") is True
    assert wg.route_inbound_packet("pub_peer_A", "10.0.0.99") is False
    print("Day 331 WireGuard tests passed!")
