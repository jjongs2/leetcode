class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count = sum(nums)
        if count == 0:
            return 0
        nums.extend(nums)
        partial_count = sum(nums[:count])
        max_partial_count = partial_count
        for i in range(len(nums) - count):
            partial_count += nums[i + count] - nums[i]
            max_partial_count = max(max_partial_count, partial_count)
        return count - max_partial_count
