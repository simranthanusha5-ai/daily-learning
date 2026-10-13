"""Day 182: Rope Data Structure for Text."""

class RopeNode:
    def __init__(self, val=""):
        self.val = val
        self.weight = len(val)
        self.left = None
        self.right = None

class Rope:
    def __init__(self, text=""):
        self.root = RopeNode(text) if text else None

    @staticmethod
    def concat(rope1, rope2):
        if not rope1.root: return rope2
        if not rope2.root: return rope1
        new_root = RopeNode()
        new_root.left = rope1.root
        new_root.right = rope2.root
        new_root.weight = Rope._total_len(rope1.root)
        r = Rope()
        r.root = new_root
        return r

    @staticmethod
    def _total_len(node):
        if not node: return 0
        if not node.left and not node.right: return node.weight
        return Rope._total_len(node.left) + Rope._total_len(node.right)

    def char_at(self, idx):
        def _get(node, i):
            if not node: return None
            if not node.left and not node.right:
                return node.val[i] if i < len(node.val) else None
            if i < node.weight:
                return _get(node.left, i)
            else:
                return _get(node.right, i - node.weight)
        return _get(self.root, idx)

if __name__ == "__main__":
    r1 = Rope("Hello_")
    r2 = Rope("World!")
    r3 = Rope.concat(r1, r2)
    assert r3.char_at(0) == "H"
    assert r3.char_at(6) == "W"
    print("Day 182 Rope tests passed!")
