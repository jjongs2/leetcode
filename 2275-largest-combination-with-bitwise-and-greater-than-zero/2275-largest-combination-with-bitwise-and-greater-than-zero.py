class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        sizes = [0 for _ in range(24)]
        for candidate in candidates:
            i = 0
            while candidate > 0:
                if candidate & 1:
                    sizes[i] += 1
                candidate >>= 1
                i += 1
        return max(sizes)
