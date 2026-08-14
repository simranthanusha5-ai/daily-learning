# Day 64: Tree Traversals (DFS)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(node):
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []

def preorder(node):
    return [node.val] + preorder(node.left) + preorder(node.right) if node else []

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("In-order traversal:  ", inorder(root))
print("Pre-order traversal: ", preorder(root))
