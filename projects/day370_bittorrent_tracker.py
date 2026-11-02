"""Day 370: BitTorrent Tracker."""

class BitTorrentTracker:
    def __init__(self):
        self.swarms = {} # info_hash -> list of {peer_id, ip, port}

    def announce(self, info_hash, peer_id, ip, port):
        swarm = self.swarms.setdefault(info_hash, [])
        for p in swarm:
            if p["peer_id"] == peer_id:
                p["ip"], p["port"] = ip, port
                return [peer for peer in swarm if peer["peer_id"] != peer_id]
        swarm.append({"peer_id": peer_id, "ip": ip, "port": port})
        return [peer for peer in swarm if peer["peer_id"] != peer_id]

if __name__ == "__main__":
    tracker = BitTorrentTracker()
    peers1 = tracker.announce("hash1", "peerA", "1.1.1.1", 6881)
    assert len(peers1) == 0
    peers2 = tracker.announce("hash1", "peerB", "2.2.2.2", 6882)
    assert len(peers2) == 1
    assert peers2[0]["peer_id"] == "peerA"
    print("Day 370 BitTorrent Tracker tests passed!")
