class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        return pow(20, n // 2, mod) * (5 if n % 2 == 1 else 1) % mod
