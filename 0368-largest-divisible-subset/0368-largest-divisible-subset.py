class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        sizes = [1] * n
        prevs = [-1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and sizes[i] < sizes[j] + 1:
                    sizes[i] = sizes[j] + 1
                    prevs[i] = j
        i, size = max(enumerate(sizes), key=lambda x: x[1])
        result = [0] * size
        for k in range(size):
            result[k] = nums[i]
            i = prevs[i]
        return result
