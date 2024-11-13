from bisect import bisect, bisect_left


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count = 0
        nums.sort()
        for i, num in enumerate(nums, start=1):
            count += bisect(nums, upper - num, i) - bisect_left(nums, lower - num, i)
        return count
