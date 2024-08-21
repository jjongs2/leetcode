class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(c for i, c in enumerate(s) if i == 0 or c != s[i - 1])
        n = len(s)
        dp = [[1 for _ in range(n)] for _ in range(n)]
        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = dp[i][j - 1] + 1
                for k in range(i, j - 1):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])
        return dp[0][-1]
