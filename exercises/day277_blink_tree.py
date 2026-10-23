"""Day 277: Lehman-Yao B-Link Tree."""

class BLinkNode:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        self.high_key = None
        self.right_link = None

class BLinkTree:
    def __init__(self, max_keys=3):
        self.root = BLinkNode(is_leaf=True)
        self.max_keys = max_keys

    def search(self, key):
        curr = self.root
        while not curr.is_leaf:
            while curr.high_key is not None and key > curr.high_key and curr.right_link:
                curr = curr.right_link
            idx = 0
            while idx < len(curr.keys) and key >= curr.keys[idx]:
                idx += 1
            curr = curr.children[idx]
        while curr.high_key is not None and key > curr.high_key and curr.right_link:
            curr = curr.right_link
        return key in curr.keys

    def insert(self, key):
        curr = self.root
        if key not in curr.keys:
            curr.keys.append(key)
            curr.keys.sort()
            if len(curr.keys) > self.max_keys:
                mid = len(curr.keys) // 2
                new_sibling = BLinkNode(is_leaf=curr.is_leaf)
                new_sibling.keys = curr.keys[mid:]
                new_sibling.high_key = curr.high_key
                new_sibling.right_link = curr.right_link
                curr.keys = curr.keys[:mid]
                curr.high_key = curr.keys[-1]
                curr.right_link = new_sibling

if __name__ == "__main__":
    tree = BLinkTree(max_keys=2)
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    assert tree.search(10) is True
    assert tree.search(30) is True
    assert tree.search(40) is False
    print("Day 277 B-Link Tree tests passed!")
