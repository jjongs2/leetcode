from heapq import heappop, heappush
from math import inf


class Solution:
    DIRECTIONS = ((1, 0, 1), (2, 0, -1), (3, 1, 0), (4, -1, 0))

    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[inf] * n for _ in range(m)]
        visited[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            w0, r0, c0 = heappop(heap)
            if w0 > visited[r0][c0]:
                continue
            for i, dr, dc in self.DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if not (0 <= r < m and 0 <= c < n):
                    continue
                w = w0 if i == grid[r0][c0] else w0 + 1
                if w >= visited[r][c]:
                    continue
                visited[r][c] = w
                heappush(heap, (w, r, c))
        return visited[-1][-1]
