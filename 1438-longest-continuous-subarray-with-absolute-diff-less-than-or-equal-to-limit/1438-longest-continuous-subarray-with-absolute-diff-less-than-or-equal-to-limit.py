from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_length = 0
        start = 0
        max_deq, min_deq = deque(), deque()
        for end, num in enumerate(nums):
            while max_deq and num > max_deq[-1]:
                max_deq.pop()
            max_deq.append(num)
            while min_deq and num < min_deq[-1]:
                min_deq.pop()
            min_deq.append(num)
            while max_deq[0] - min_deq[0] > limit:
                if max_deq[0] == nums[start]:
                    max_deq.popleft()
                if min_deq[0] == nums[start]:
                    min_deq.popleft()
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length
