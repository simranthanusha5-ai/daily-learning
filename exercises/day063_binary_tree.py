# Day 63: Binary Tree Structure

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Construct tree:
#       1
#      / \
#     2   3
#    /
#   4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(f"Root: {root.val}, Left Child: {root.left.val}, Right Child: {root.right.val}")
