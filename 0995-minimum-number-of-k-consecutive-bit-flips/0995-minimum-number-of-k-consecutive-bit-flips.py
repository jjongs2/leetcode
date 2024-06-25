from collections import deque


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        nums_length = len(nums)
        flip_count = 0
        flip_queue = deque()
        for i, num in enumerate(nums):
            if flip_queue and flip_queue[0] + k == i:
                flip_queue.popleft()
            if (num + len(flip_queue)) & 1 == 1:
                continue
            if i + k > nums_length:
                return -1
            flip_queue.append(i)
            flip_count += 1
        return flip_count
