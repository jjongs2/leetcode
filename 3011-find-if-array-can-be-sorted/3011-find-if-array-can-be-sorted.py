from math import inf


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_min = curr_min = inf
        prev_max = curr_max = -inf
        prev_bits = 0
        bits = dict()
        nums.append(0)
        for num in nums:
            if num not in bits:
                bits[num] = num.bit_count()
            curr_bits = bits[num]
            if curr_bits == prev_bits:
                if num < curr_min:
                    curr_min = num
                elif num > curr_max:
                    curr_max = num
                continue
            if prev_max > curr_min:
                return False
            prev_bits = curr_bits
            prev_min, prev_max = curr_min, curr_max
            curr_min = curr_max = num
        return True
