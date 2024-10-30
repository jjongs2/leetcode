DIRECTIONS = ((-1, 1), (0, 1), (1, 1))


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for c in range(1, n):
            prev_count = count
            for r in range(m):
                curr = grid[r][c]
                for dr, dc in DIRECTIONS:
                    r0, c0 = r - dr, c - dc
                    if not (0 <= r0 < m and 0 <= c0 < n):
                        continue
                    if grid[r0][c0] < curr and dp[r0][c0] + 1 > dp[r][c]:
                        x = dp[r][c] = dp[r0][c0] + 1
                        count = max(count, x)
            if count == prev_count:
                break
        return count
