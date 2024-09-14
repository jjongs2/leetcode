class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = length = 0
        max_num = 0
        for num in nums:
            if num < max_num:
                length = 0
            elif num > max_num:
                max_num = num
                max_length = length = 1
            else:
                length += 1
                max_length = max(max_length, length)
        return max_length
