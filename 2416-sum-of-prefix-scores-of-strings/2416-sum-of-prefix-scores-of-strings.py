from collections import defaultdict


class TrieNode:
    __slots__ = ("score", "children")

    def __init__(self):
        self.score = 0
        self.children = defaultdict(TrieNode)


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                node = node.children[char]
                node.score += 1

        def sum_score(word):
            total_score = 0
            node = root
            for char in word:
                node = node.children[char]
                total_score += node.score
            return total_score

        return [sum_score(word) for word in words]
