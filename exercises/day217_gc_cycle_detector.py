"""Day 217: GC Cycle Detection."""

class GCObject:
    def __init__(self, name):
        self.name = name
        self.refs = []
        self.ref_count = 0

    def add_ref(self, target):
        self.refs.append(target)
        target.ref_count += 1

def detect_cycles(objects):
    trial_counts = {obj: obj.ref_count for obj in objects}
    for obj in objects:
        for ref in obj.refs:
            trial_counts[ref] -= 1
    unreachable = [obj for obj, count in trial_counts.items() if count == 0]
    return unreachable

if __name__ == "__main__":
    o1 = GCObject("o1")
    o2 = GCObject("o2")
    o1.add_ref(o2)
    o2.add_ref(o1)
    unreachable = detect_cycles([o1, o2])
    assert len(unreachable) == 2
    print("Day 217 GC Cycle tests passed!")
