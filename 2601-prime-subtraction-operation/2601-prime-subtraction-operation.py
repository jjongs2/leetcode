from bisect import bisect


class Solution:
    BOUND = 1001

    def __init__(self):
        self.primes_set = self._find_primes()
        self.primes = sorted(self.primes_set)

    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = self.BOUND
        for curr in reversed(nums):
            if curr >= prev:
                min_val = curr - prev + 1
                if min_val > self.primes[-1]:
                    return False
                if min_val in self.primes_set:
                    curr -= min_val
                else:
                    curr -= self.primes[bisect(self.primes, min_val)]
                if curr <= 0:
                    return False
            prev = curr
        return True

    def _find_primes(self) -> set:
        primes = set(range(2, self.BOUND))
        for i in range(2, self.BOUND):
            if i not in primes:
                continue
            for j in range(i * i, self.BOUND, i):
                primes.discard(j)
        return primes
