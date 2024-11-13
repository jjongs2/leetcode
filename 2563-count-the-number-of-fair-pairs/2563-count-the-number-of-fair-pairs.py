from bisect import bisect_left, bisect_right


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count = 0
        nums.sort()
        for i, num in enumerate(nums):
            left = bisect_left(nums, lower - num)
            right = bisect_right(nums, upper - num)
            count += right - left
            if left <= i < right:
                count -= 1
        return count // 2
