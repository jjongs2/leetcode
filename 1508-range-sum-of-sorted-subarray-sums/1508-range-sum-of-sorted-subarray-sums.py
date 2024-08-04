from heapq import heappop, heappush, heapreplace

MOD = 10**9 + 7


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
        result = 0
        for i in range(1, right + 1):
            sub_sum, last_num_i = heap[0]
            if i >= left:
                result += sub_sum
            last_num_i += 1
            if last_num_i < n:
                sub_sum += nums[last_num_i]
                heapreplace(heap, (sub_sum, last_num_i))
            else:
                heappop(heap)
        return result % MOD
