from bisect import bisect


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0
        stack = [0]
        for i in range(1, len(nums)):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)
        for j in range(len(nums) - 1, -1, -1):
            num = nums[j]
            while stack and nums[stack[-1]] <= num:
                max_width = max(max_width, j - stack.pop())
        return max_width
