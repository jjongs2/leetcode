class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing_sum = mean * (n + m) - sum(rolls)
        if not (n <= missing_sum <= 6 * n):
            return []
        quotient, remainder = divmod(missing_sum, n)
        result = [quotient for _ in range(n)]
        for i in range(remainder):
            result[i] += 1
        return result
