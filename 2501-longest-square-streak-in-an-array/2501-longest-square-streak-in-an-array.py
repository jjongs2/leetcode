class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        streaks = dict()
        nums.sort()
        for num in nums:
            streaks[num * num] = streaks.get(num, 0) + 1
        result = max(streaks.values())
        return result if result > 1 else -1
