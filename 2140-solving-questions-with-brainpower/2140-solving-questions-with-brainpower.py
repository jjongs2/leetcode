class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        for i, (p, b) in enumerate(questions):
            dp[i] = max(dp[i], dp[i - 1])
            j = min(i + b, n - 1)
            dp[j] = max(dp[j], dp[i - 1] + p)
        return dp[-1]
