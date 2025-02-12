from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        heaps = defaultdict(list)
        for num in nums:
            digit_sum = 0
            n = num
            while n > 0:
                digit_sum += n % 10
                n //= 10
            heappush(heaps[digit_sum], -num)
        result = -1
        for heap in heaps.values():
            if len(heap) < 2:
                continue
            n1 = -heappop(heap)
            n2 = -heap[0]
            result = max(result, n1 + n2)
        return result
