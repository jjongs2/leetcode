from collections import defaultdict


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        indices = []
        i = 0
        num = k
        while num > 0:
            if num & 1:
                indices.append(i)
            num >>= 1
            i += 1
        bits = defaultdict(int)

        def is_special():
            num = 0
            for i in bits:
                num |= 1 << i
            return num >= k

        n = len(nums)
        result = n + 1
        left = right = 0
        while right < n:
            if nums[right] >= k:
                return 1
            i = 0
            num = nums[right]
            while num > 0:
                if num & 1:
                    bits[i] += 1
                num >>= 1
                i += 1
            right += 1
            while is_special():
                result = min(result, right - left)
                i = 0
                num = nums[left]
                while num > 0:
                    if num & 1:
                        if bits[i] == 1:
                            del bits[i]
                        else:
                            bits[i] -= 1
                    num >>= 1
                    i += 1
                left += 1
        return result if result <= n else -1
