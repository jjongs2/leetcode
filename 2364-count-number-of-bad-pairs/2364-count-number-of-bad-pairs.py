from collections import Counter
from math import comb


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = comb(n, 2)
        freqs = Counter(i - num for i, num in enumerate(nums))
        for freq in freqs.values():
            count -= comb(freq, 2)
        return count
