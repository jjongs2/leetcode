from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            for j in indices[num]:
                if (i * j) % k == 0:
                    result += 1
            indices[num].append(i)
        return result
