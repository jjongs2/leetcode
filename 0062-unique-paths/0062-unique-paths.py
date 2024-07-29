class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cols = [1 for _ in range(n)]
        for r in range(1, m):
            for c in range(1, n):
                cols[c] += cols[c - 1]
        return cols[-1]
