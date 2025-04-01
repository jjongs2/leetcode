class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            p, b = questions[i]
            j = min(n, i + b + 1)
            dp[i] = max(p + dp[j], dp[i + 1])
        return dp[0]
