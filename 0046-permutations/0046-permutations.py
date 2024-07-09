class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        num_count = len(nums)

        def backtrack(index):
            if index == num_count:
                result.append(nums.copy())
                return
            for i in range(index, num_count):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        backtrack(0)
        return result
