"""Day 284: Persistent Immutable BST."""

class PNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def insert_persistent(root, key):
    if not root:
        return PNode(key)
    if key < root.key:
        return PNode(root.key, insert_persistent(root.left, key), root.right)
    elif key > root.key:
        return PNode(root.key, root.left, insert_persistent(root.right, key))
    return root

def search_persistent(root, key):
    if not root: return False
    if root.key == key: return True
    return search_persistent(root.left if key < root.key else root.right, key)

if __name__ == "__main__":
    v0 = None
    v1 = insert_persistent(v0, 20)
    v2 = insert_persistent(v1, 10)
    v3 = insert_persistent(v2, 30)
    assert search_persistent(v1, 30) is False
    assert search_persistent(v3, 30) is True
    print("Day 284 Persistent BST tests passed!")
