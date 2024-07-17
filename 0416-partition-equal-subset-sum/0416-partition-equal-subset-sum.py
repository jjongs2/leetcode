class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        sums = {0}
        for num in nums:
            sums |= {s + num for s in sums if s + num <= target}
            if target in sums:
                return True
        return False
