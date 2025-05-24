class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        p = [0] * (n + 1)
        for l, r in queries:
            p[l] += 1
            p[r + 1] -= 1
        for i in range(n):
            if p[i] < nums[i]:
                return False
            p[i + 1] += p[i]
        return True
