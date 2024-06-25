class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        length = len(nums)
        flips = [0 for _ in range(length)]
        flip = 0
        for i, num in enumerate(nums):
            if i - k >= 0:
                flip ^= flips[i - k]
            if num != flip:
                continue
            if i + k > length:
                return -1
            flip ^= 1
            flips[i] = 1
        return sum(flips)
