"""Day 285: Cartesian Tree."""

class CTreeNode:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    stack = []
    for i, val in enumerate(arr):
        node = CTreeNode(val, i)
        last_popped = None
        while stack and stack[-1].val > val:
            last_popped = stack.pop()
        node.left = last_popped
        if stack:
            stack[-1].right = node
        stack.append(node)
    return stack[0] if stack else None

if __name__ == "__main__":
    nums = [3, 2, 6, 1, 9]
    root = build_cartesian_tree(nums)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 9
    print("Day 285 Cartesian Tree tests passed!")
