from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for b in words2:
            counter |= Counter(b)
        return [a for a in words1 if Counter(a) >= counter]
