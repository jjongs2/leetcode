class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 0
        left = 0
        x = 0
        for right in range(len(nums)):
            while x & nums[right]:
                x ^= nums[left]
                left += 1
            x ^= nums[right]
            result = max(result, right - left + 1)
        return result
