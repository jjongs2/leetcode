from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num == 0 for num in nums):
            return "0"

        def compare(a, b):
            lhs, rhs = a + b, b + a
            if lhs < rhs:
                return 1
            if lhs > rhs:
                return -1
            return 0

        return "".join(sorted(map(str, nums), key=cmp_to_key(compare)))
