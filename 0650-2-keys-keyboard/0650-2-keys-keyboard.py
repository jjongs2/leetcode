from math import isqrt


class Solution:
    def __init__(self):
        self.memo = {1: 0}

    def minSteps(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                self.memo[n] = self.minSteps(n // i) + i
                break
        else:
            self.memo[n] = n
        return self.memo[n]
