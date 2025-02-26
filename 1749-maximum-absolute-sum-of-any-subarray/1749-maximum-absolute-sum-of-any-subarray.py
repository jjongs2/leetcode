class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_val = max_val = 0
        for num in nums:
            prefix_sum += num
            min_val = min(min_val, prefix_sum)
            max_val = max(max_val, prefix_sum)
        return max_val - min_val
