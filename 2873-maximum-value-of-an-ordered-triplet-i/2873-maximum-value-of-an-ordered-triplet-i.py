from itertools import combinations


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        return max(0, max((a - b) * c for a, b, c in combinations(nums, 3)))
