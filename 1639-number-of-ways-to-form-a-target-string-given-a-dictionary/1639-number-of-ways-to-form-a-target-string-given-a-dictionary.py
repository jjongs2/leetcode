from collections import Counter


class Solution:
    MOD = 10**9 + 7

    def numWays(self, words: List[str], target: str) -> int:
        w, t = len(words[0]), len(target)
        counters = tuple(map(Counter, zip(*words)))
        dp = [[0] * (w + 1) for _ in range(t + 1)]
        for k in range(w + 1):
            dp[0][k] = 1
        for i, t_char in enumerate(target, start=1):
            for k in range(1, w + 1):
                dp[i][k] = dp[i][k - 1]
                counter = counters[k - 1]
                if t_char not in counter:
                    continue
                dp[i][k] += dp[i - 1][k - 1] * counter[t_char]
                dp[i][k] %= self.MOD
        return dp[-1][-1]
