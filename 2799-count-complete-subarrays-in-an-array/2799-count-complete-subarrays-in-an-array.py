from collections import Counter


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_count = len(set(nums))
        freqs = Counter()
        result = 0
        left = 0
        for right in range(n):
            freqs[nums[right]] += 1
            while len(freqs) == distinct_count:
                result += n - right
                if freqs[nums[left]] == 1:
                    del freqs[nums[left]]
                else:
                    freqs[nums[left]] -= 1
                left += 1
        return result
