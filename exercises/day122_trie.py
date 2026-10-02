# Day 122: Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

trie = Trie()
trie.insert("python")
trie.insert("programming")
print("Search 'python':", trie.search("python"))
print("Search 'pro':", trie.search("pro"))
print("Starts with 'pro':", trie.starts_with("pro"))
