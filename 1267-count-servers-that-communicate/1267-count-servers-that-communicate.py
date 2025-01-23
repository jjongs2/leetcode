from itertools import product


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_counts = [0] * m
        col_counts = [0] * n
        pos = []
        for r, c in product(range(m), range(n)):
            if grid[r][c] == 1:
                row_counts[r] += 1
                col_counts[c] += 1
                pos.append((r, c))
        count = 0
        for r, c in pos:
            if row_counts[r] >= 2 or col_counts[c] >= 2:
                count += 1
        return count
