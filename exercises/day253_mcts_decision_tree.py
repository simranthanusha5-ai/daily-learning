"""Day 253: Monte Carlo Tree Search Node."""
import math

class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0

    def ucb1(self, c=1.414):
        if self.visits == 0:
            return float('inf')
        return (self.value / self.visits) + c * math.sqrt(math.log(self.parent.visits) / self.visits)

    def backpropagate(self, reward):
        self.visits += 1
        self.value += reward
        if self.parent:
            self.parent.backpropagate(reward)

if __name__ == "__main__":
    root = MCTSNode("ROOT")
    c1 = MCTSNode("C1", parent=root)
    root.visits = 10
    c1.visits = 5
    c1.value = 4.0
    assert c1.ucb1() > 0.8
    print("Day 253 MCTS tests passed!")
