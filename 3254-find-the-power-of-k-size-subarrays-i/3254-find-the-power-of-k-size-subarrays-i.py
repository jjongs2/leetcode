class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = [-1 for _ in range(n - k + 1)]
        count = 0
        prev = -1
        for i, curr in enumerate(nums):
            count = count + 1 if curr == prev + 1 else 1
            if count >= k:
                results[i - k + 1] = curr
            prev = curr
        return results
