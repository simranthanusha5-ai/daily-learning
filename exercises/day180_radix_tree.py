"""Day 180: Radix Tree."""

class RadixNode:
    def __init__(self, prefix=""):
        self.prefix = prefix
        self.is_leaf = False
        self.children = {}

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, word):
        curr = self.root
        i = 0
        while i < len(word):
            char = word[i]
            if char not in curr.children:
                new_node = RadixNode(word[i:])
                new_node.is_leaf = True
                curr.children[char] = new_node
                return
            child = curr.children[char]
            j = 0
            while j < len(child.prefix) and i + j < len(word) and child.prefix[j] == word[i + j]:
                j += 1
            if j < len(child.prefix):
                split_node = RadixNode(child.prefix[:j])
                child.prefix = child.prefix[j:]
                split_node.children[child.prefix[0]] = child
                curr.children[char] = split_node
                if i + j == len(word):
                    split_node.is_leaf = True
                else:
                    leaf = RadixNode(word[i + j:])
                    leaf.is_leaf = True
                    split_node.children[word[i + j]] = leaf
                return
            else:
                i += j
                curr = child
        curr.is_leaf = True

    def search(self, word):
        curr = self.root
        i = 0
        while i < len(word):
            char = word[i]
            if char not in curr.children:
                return False
            child = curr.children[char]
            if not word[i:].startswith(child.prefix):
                return False
            i += len(child.prefix)
            curr = child
        return curr.is_leaf

if __name__ == "__main__":
    rt = RadixTree()
    rt.insert("apple")
    rt.insert("app")
    rt.insert("apply")
    assert rt.search("apple") is True
    assert rt.search("app") is True
    assert rt.search("application") is False
    print("Day 180 Radix Tree tests passed!")
