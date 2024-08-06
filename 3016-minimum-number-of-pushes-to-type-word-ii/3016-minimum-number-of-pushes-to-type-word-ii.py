from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = sorted(Counter(word).values(), reverse=True)
        return sum(cost * (i // 8 + 1) for i, cost in enumerate(counts))
