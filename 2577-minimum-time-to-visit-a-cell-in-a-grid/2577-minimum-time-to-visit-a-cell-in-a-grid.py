from heapq import heappush, heappop
from math import inf


class Solution:
    DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        m, n = len(grid), len(grid[0])
        visited = [[inf] * n for _ in range(m)]
        visited[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            v0, r0, c0 = heappop(heap)
            if v0 > visited[r0][c0]:
                continue
            for dr, dc in self.DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if not (0 <= r < m and 0 <= c < n):
                    continue
                v = v0 + (max(0, grid[r][c] - v0) | 1)
                if (r, c) == (m - 1, n - 1):
                    return v
                if v >= visited[r][c]:
                    continue
                visited[r][c] = v
                heappush(heap, (v, r, c))
