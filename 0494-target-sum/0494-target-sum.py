from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prevs = {0: 1}
        for num in nums:
            currs = defaultdict(int)
            for k, v in prevs.items():
                currs[k + num] += v
                currs[k - num] += v
            prevs = currs
        return prevs[target]
