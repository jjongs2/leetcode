class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for bits in range(1 << n):
            xor = 0
            for i in range(n):
                if bits & (1 << i):
                    xor ^= nums[i]
            result += xor
        return result
