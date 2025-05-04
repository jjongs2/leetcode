from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freqs = Counter(map(lambda x: (1 << x[0]) + (1 << x[1]), dominoes))
        return sum(n * (n - 1) // 2 for n in freqs.values())
