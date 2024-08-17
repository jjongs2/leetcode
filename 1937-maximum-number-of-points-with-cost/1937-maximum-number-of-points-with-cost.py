from itertools import product


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        for r in range(m - 1):
            row = points[r]
            for c in range(n - 2, -1, -1):
                row[c] = max(row[c], row[c + 1] - 1)
            points[r + 1][0] += row[0]
            for c in range(1, n):
                row[c] = max(row[c], row[c - 1] - 1)
                points[r + 1][c] += row[c]
        return max(points[-1])
