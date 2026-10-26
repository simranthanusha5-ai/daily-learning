"""Day 310: EPaxos Dependency Tracker."""

class EPaxosInstance:
    def __init__(self, inst_id, cmd, deps):
        self.inst_id = inst_id
        self.cmd = cmd
        self.deps = set(deps)

def execute_epaxos(instances):
    adj = {i.inst_id: i.deps for i in instances}
    visited = set()
    order = []

    def dfs(u):
        visited.add(u)
        for v in adj.get(u, []):
            if v not in visited and v in adj:
                dfs(v)
        order.append(u)

    for i in instances:
        if i.inst_id not in visited:
            dfs(i.inst_id)
    return order

if __name__ == "__main__":
    i1 = EPaxosInstance("C1", "W x=1", [])
    i2 = EPaxosInstance("C2", "W x=2", ["C1"])
    i3 = EPaxosInstance("C3", "W y=5", [])
    seq = execute_epaxos([i1, i2, i3])
    assert seq.index("C1") < seq.index("C2")
    print("Day 310 EPaxos tests passed!")
