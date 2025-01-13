from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counter = Counter(s)
        odds = sum(count % 2 == 1 for count in counter.values())
        return odds <= k
