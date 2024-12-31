class Solution:
    DURATIONS = (1, 7, 30)

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [inf] * (n + 1)
        dp[0] = 0
        passes = tuple(zip(self.DURATIONS, costs))
        for i, day in enumerate(days):
            for duration, cost in passes:
                j = i + 1
                while j < n and day + duration > days[j]:
                    j += 1
                dp[j] = min(dp[j], dp[i] + cost)
        return dp[-1]
