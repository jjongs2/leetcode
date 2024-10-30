from itertools import product


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for r, c in product(range(m), range(n)):
            if matrix[r][c] == 0:
                continue
            x = dp[r + 1][c + 1] = min(dp[r][c], dp[r][c + 1], dp[r + 1][c]) + 1
            count += x
        return count
