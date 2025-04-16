from collections import defaultdict


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        freqs = defaultdict(int)
        pair_count = 0
        left = 0
        for right in range(n):
            pair_count += freqs[nums[right]]
            freqs[nums[right]] += 1
            while pair_count >= k:
                result += n - right
                freqs[nums[left]] -= 1
                pair_count -= freqs[nums[left]]
                left += 1
        return result
