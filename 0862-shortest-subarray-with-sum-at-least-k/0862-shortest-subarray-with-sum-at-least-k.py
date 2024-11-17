from collections import deque
from math import inf


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        psums = [0 for _ in range(n + 1)]
        for i, num in enumerate(nums):
            psums[i + 1] = psums[i] + num
        result = inf
        lefts = deque()
        for right in range(n + 1):
            while lefts and psums[right] <= psums[lefts[-1]]:
                lefts.pop()
            while lefts and psums[right] - psums[lefts[0]] >= k:
                result = min(result, right - lefts.popleft())
            lefts.append(right)
        return result if result < inf else -1
