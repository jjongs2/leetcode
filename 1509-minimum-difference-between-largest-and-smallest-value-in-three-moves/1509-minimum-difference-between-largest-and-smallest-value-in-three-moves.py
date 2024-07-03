class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        s = sorted(nums)
        return min(s[-1] - s[3], s[-2] - s[2], s[-3] - s[1], s[-4] - s[0])
