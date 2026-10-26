"""Day 311: Distributed Deadlock Detection."""

class DeadlockDetector:
    def __init__(self):
        self.wait_for = {} # initiator -> set of holding transactions

    def add_dependency(self, waiting_tx, holding_tx):
        self.wait_for.setdefault(waiting_tx, set()).add(holding_tx)

    def detect_cycle(self):
        visited = set()
        rec_stack = set()

        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            for neighbor in self.wait_for.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(node)
            return False

        for n in list(self.wait_for.keys()):
            if n not in visited:
                if dfs(n):
                    return True
        return False

if __name__ == "__main__":
    dd = DeadlockDetector()
    dd.add_dependency("T1", "T2")
    dd.add_dependency("T2", "T3")
    dd.add_dependency("T3", "T1")
    assert dd.detect_cycle() is True
    print("Day 311 Deadlock Detection tests passed!")
