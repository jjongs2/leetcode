class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for n in range(low, high + 1):
            if 10 <= n < 100 and n // 10 == n % 10:
                count += 1
            elif (
                1000 <= n < 10000
                and n // 1000 + (n // 100) % 10 == (n // 10 % 10) + n % 10
            ):
                count += 1
        return count
