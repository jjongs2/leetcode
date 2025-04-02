class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        m, diff = 0, 0
        for num in nums:
            result = max(result, diff * num)
            diff = max(diff, m - num)
            m = max(m, num)
        return result
