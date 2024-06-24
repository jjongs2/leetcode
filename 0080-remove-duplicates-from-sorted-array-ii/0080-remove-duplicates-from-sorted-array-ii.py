class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if count == 2:
                    continue
                count += 1
            else:
                count = 1
            nums[k] = nums[i]
            k += 1
        return k
