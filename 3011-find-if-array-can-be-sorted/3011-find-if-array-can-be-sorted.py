from math import inf


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = curr_max = -inf
        prev_bits = 0
        bits = dict()
        for num in nums:
            curr_bits = bits.setdefault(num, num.bit_count())
            if curr_bits == prev_bits:
                if num < prev_max:
                    return False
                curr_max = max(curr_max, num)
                continue
            if num < curr_max:
                return False
            prev_max = curr_max
            curr_max = num
            prev_bits = curr_bits
        return True
