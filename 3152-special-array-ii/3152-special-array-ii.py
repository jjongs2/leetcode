class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        results = []
        n = len(nums)
        prefix_sums = [0] * n
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i - 1] + ((nums[i] ^ nums[i - 1]) & 1)
        for s, e in queries:
            results.append(prefix_sums[e] - prefix_sums[s] == e - s)
        return results
