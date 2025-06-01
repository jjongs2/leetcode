from math import comb


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def H(n, k):
            if k < 0:
                return 0
            return comb(n + k - 1, k)

        x = limit + 1
        return H(3, n) - 3 * H(3, n - x) + 3 * H(3, n - 2 * x) - H(3, n - 3 * x)
