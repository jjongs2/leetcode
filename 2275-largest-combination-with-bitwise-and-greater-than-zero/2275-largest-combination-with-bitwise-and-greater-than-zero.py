class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        sizes = dict()
        for candidate in candidates:
            i = 1
            while i <= candidate:
                if candidate & i:
                    sizes[i] = sizes.get(i, 0) + 1
                i <<= 1
        return max(sizes.values())
