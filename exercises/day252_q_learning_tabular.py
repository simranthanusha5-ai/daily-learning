"""Day 252: Tabular Q-Learning."""
from collections import defaultdict

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9):
        self.q_table = defaultdict(float)
        self.alpha = alpha
        self.gamma = gamma

    def update(self, state, action, reward, next_state, possible_next_actions):
        current_q = self.q_table[(state, action)]
        max_next_q = max([self.q_table[(next_state, a)] for a in possible_next_actions], default=0.0)
        td_target = reward + self.gamma * max_next_q
        self.q_table[(state, action)] += self.alpha * (td_target - current_q)

if __name__ == "__main__":
    agent = QLearningAgent()
    agent.update("s0", "a0", reward=10.0, next_state="s1", possible_next_actions=["a1"])
    assert agent.q_table[("s0", "a0")] == 1.0
    print("Day 252 Q-Learning tests passed!")
