class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices:
                return [indices[diff], i]
            indices[num] = i
