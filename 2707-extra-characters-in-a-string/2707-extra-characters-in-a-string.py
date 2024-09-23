class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        s_len = len(s)
        dp = [0 for _ in range(s_len + 1)]
        for j in range(1, s_len + 1):
            generator = (dp[i] for i in range(j) if s[i:j] in words)
            dp[j] = min(dp[j - 1] + 1, min(generator, default=j))
        return dp[-1]
