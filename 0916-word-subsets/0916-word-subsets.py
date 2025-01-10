from collections import Counter
from functools import reduce


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = reduce(lambda x, y: x | y, map(Counter, words2))
        return [a for a in words1 if Counter(a) >= counter]
