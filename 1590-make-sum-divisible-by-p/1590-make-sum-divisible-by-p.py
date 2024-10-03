class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_r = sum(nums) % p
        if total_r == 0:
            return 0
        min_len = len(nums)
        indices = {0: -1}
        r = 0
        for i, num in enumerate(nums):
            r = (r + num) % p
            target_r = (r - total_r) % p
            if target_r in indices:
                min_len = min(min_len, i - indices[target_r])
            indices[r] = i
        return min_len if min_len < len(nums) else -1
