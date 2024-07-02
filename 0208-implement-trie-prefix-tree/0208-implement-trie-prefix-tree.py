class Trie:
    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            curr = curr.setdefault(char, dict())
        curr["\0"] = None

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if not (curr := curr.get(char)):
                return False
        return "\0" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if not (curr := curr.get(char)):
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
