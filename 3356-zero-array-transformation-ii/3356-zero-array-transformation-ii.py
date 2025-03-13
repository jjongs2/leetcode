class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        prefix_sums = [0] * (len(nums) + 1)
        q = len(queries)
        k = 0
        for i, num in enumerate(nums):
            while prefix_sums[i] < num:
                if k == q:
                    return -1
                left, right, val = queries[k]
                if i <= right:
                    prefix_sums[max(left, i)] += val
                    prefix_sums[right + 1] -= val
                k += 1
            prefix_sums[i + 1] += prefix_sums[i]
        return k
