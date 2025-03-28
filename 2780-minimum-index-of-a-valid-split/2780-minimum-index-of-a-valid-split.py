from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freqs = Counter(nums)
        dominant = max(freqs, key=lambda x: freqs[x])
        if freqs[dominant] <= n // 2:
            return -1
        left, right = 0, freqs[dominant]
        for i, num in enumerate(nums, start=1):
            if num == dominant:
                left += 1
                right -= 1
                if left > i // 2 and right > (n - i) // 2:
                    return i - 1
        return -1
