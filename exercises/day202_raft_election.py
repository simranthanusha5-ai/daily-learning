"""Day 202: Raft Leader Election."""

class RaftNode:
    FOLLOWER = 0
    CANDIDATE = 1
    LEADER = 2

    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.term = 0
        self.voted_for = None
        self.role = self.FOLLOWER

    def start_election(self):
        self.role = self.CANDIDATE
        self.term += 1
        self.voted_for = self.node_id
        votes = 1
        for peer in self.peers:
            if peer.request_vote(self.node_id, self.term):
                votes += 1
        if votes > (len(self.peers) + 1) // 2:
            self.role = self.LEADER

    def request_vote(self, candidate_id, term):
        if term > self.term:
            self.term = term
            self.role = self.FOLLOWER
            self.voted_for = None
        if term == self.term and (self.voted_for is None or self.voted_for == candidate_id):
            self.voted_for = candidate_id
            return True
        return False

if __name__ == "__main__":
    nodes = [RaftNode(i, []) for i in range(3)]
    for n in nodes:
        n.peers = [peer for peer in nodes if peer != n]
    nodes[0].start_election()
    assert nodes[0].role == RaftNode.LEADER
    print("Day 202 Raft Election tests passed!")
