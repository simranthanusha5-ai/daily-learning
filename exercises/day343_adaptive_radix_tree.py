"""Day 343: Adaptive Radix Tree (ART)."""

class ARTNode4:
    def __init__(self):
        self.keys = []
        self.children = []

    def add(self, byte_val, child):
        if len(self.keys) < 4:
            self.keys.append(byte_val)
            self.children.append(child)
            return self
        # Grow to Node16
        n16 = ARTNode16()
        n16.keys = list(self.keys) + [byte_val]
        n16.children = list(self.children) + [child]
        return n16

class ARTNode16:
    def __init__(self):
        self.keys = []
        self.children = []

if __name__ == "__main__":
    node = ARTNode4()
    for b in [ord('a'), ord('b'), ord('c'), ord('d')]:
        node = node.add(b, f"child_{chr(b)}")
    assert isinstance(node, ARTNode4)
    node = node.add(ord('e'), "child_e")
    assert isinstance(node, ARTNode16)
    print("Day 343 ART tests passed!")
