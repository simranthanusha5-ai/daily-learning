"""Day 203: Gossip Protocol Node."""
import random

class GossipNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.membership = {node_id: 0} # {id: heartbeat}

    def heartbeat(self):
        self.membership[self.node_id] += 1

    def gossip(self, peer):
        peer.receive_gossip(self.membership)

    def receive_gossip(self, incoming):
        for nid, count in incoming.items():
            if nid not in self.membership or count > self.membership[nid]:
                self.membership[nid] = count

if __name__ == "__main__":
    n1 = GossipNode(1)
    n2 = GossipNode(2)
    n1.heartbeat()
    n1.heartbeat()
    n1.gossip(n2)
    assert n2.membership[1] == 2
    print("Day 203 Gossip Protocol tests passed!")
