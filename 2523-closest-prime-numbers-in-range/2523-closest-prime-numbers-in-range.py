from math import isqrt


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        is_prime[1] = False
        for i in range(2, isqrt(right) + 1):
            if not is_prime[i]:
                continue
            for num in range(i * i, right + 1, i):
                is_prime[num] = False
        result = [-1, -1]
        diff = right
        prev = -right
        for curr in range(left, right + 1):
            if not is_prime[curr]:
                continue
            if curr - prev < diff:
                diff = curr - prev
                result = [prev, curr]
            prev = curr
        return result
