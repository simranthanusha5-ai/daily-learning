# Day 65: Tree Level-Order Traversal (BFS)
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

root = TreeNode("A")
root.left, root.right = TreeNode("B"), TreeNode("C")
root.left.left, root.left.right = TreeNode("D"), TreeNode("E")
print("Level-order:", level_order(root))
