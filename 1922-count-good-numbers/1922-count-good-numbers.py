class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        exp = (n // 2) % (mod - 1)
        base = 20
        count = 1
        while exp > 0:
            if exp % 2 == 1:
                count = (count * base) % mod
            base = (base * base) % mod
            exp //= 2
        if n % 2 == 1:
            count = (count * 5) % mod
        return count
