class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        i = 0
        for j in range(n - 1):
            if nums[j] == nums[j + 1]:
                nums[j] *= 2
                nums[j + 1] = 0
            if nums[j] > 0:
                result[i] = nums[j]
                i += 1
        result[i] = nums[-1]
        return result
