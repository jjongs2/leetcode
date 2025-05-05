class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        mod = 10**9 + 7
        tb = [0] * n
        t = [0] * n
        b = [0] * n
        tb[0], tb[1] = 1, 2
        t[1] = 1
        b[1] = 1
        for i in range(2, n):
            tb[i] = (tb[i - 1] + tb[i - 2] + t[i - 1] + b[i - 1]) % mod
            t[i] = (b[i - 1] + tb[i - 2]) % mod
            b[i] = (t[i - 1] + tb[i - 2]) % mod
        return tb[-1]
