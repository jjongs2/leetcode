class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = max(nums) - k + 1
        if n <= 0:
            return len(nums)
        changes = [0] * n
        for num in nums:
            start, end = num - k, num + k + 1
            changes[max(0, start)] += 1
            if end < n:
                changes[end] -= 1
        result = 1
        cumul_sum = 0
        for change in changes:
            cumul_sum += change
            result = max(result, cumul_sum)
        return result
