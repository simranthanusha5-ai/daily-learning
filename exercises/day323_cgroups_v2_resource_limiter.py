"""Day 323: cgroups v2 Tree."""

class CGroupNode:
    def __init__(self, name, max_memory=float('inf'), parent=None):
        self.name = name
        self.max_memory = max_memory
        self.parent = parent
        self.current_memory = 0
        self.children = []

    def add_child(self, name, max_memory=float('inf')):
        child = CGroupNode(name, min(self.max_memory, max_memory), parent=self)
        self.children.append(child)
        return child

    def charge(self, amount):
        if self.current_memory + amount > self.max_memory:
            raise MemoryError(f"cgroup {self.name} exceeded memory limit")
        if self.parent:
            self.parent.charge(amount)
        self.current_memory += amount

if __name__ == "__main__":
    root = CGroupNode("root", max_memory=100)
    web = root.add_child("web_service", max_memory=60)
    web.charge(50)
    assert root.current_memory == 50
    try:
        web.charge(20) # 70 > 60
        assert False
    except MemoryError:
        pass
    print("Day 323 cgroups v2 tests passed!")
