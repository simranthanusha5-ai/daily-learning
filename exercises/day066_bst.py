# Day 66: Binary Search Tree (BST)

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if not root:
        return BSTNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def search_bst(root, target):
    if not root or root.val == target:
        return root is not None
    if target < root.val:
        return search_bst(root.left, target)
    return search_bst(root.right, target)

tree = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    tree = insert_bst(tree, v)

print("Search 40 in BST:", search_bst(tree, 40))
print("Search 99 in BST:", search_bst(tree, 99))
