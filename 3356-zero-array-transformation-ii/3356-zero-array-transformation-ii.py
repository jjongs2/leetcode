class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def is_possible(k):
            prefix_sums = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                prefix_sums[l] += val
                prefix_sums[r + 1] -= val
            for i in range(n):
                if prefix_sums[i] < nums[i]:
                    return False
                prefix_sums[i + 1] += prefix_sums[i]
            return True

        q = len(queries)
        low, high = -1, q + 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid
        return high if high <= q else -1
