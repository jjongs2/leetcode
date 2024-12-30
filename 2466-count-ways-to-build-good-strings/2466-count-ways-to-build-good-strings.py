class Solution:
    MOD = 10**9 + 7

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        size = high + 1
        dp = [0] * size
        dp[0] = 1
        for i in range(1, size):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= self.MOD
        return sum(dp[i] for i in range(low, size)) % self.MOD
