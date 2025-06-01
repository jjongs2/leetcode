class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0
        result = 0
        for x in range(limit + 1):
            k = n - x
            result += max(0, min(k + 1, limit - (k - limit) + 1))
        return result
