from heapq import heappop, heappush
from math import inf


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        heap = [(grid[0][0], 0, 0), (inf,)]
        result = [0] * len(queries)
        point = 0
        for q, i in sorted(((q, i) for i, q in enumerate(queries))):
            while q > heap[0][0]:
                point += 1
                _, r0, c0 = heappop(heap)
                for dr, dc in directions:
                    r, c = r0 + dr, c0 + dc
                    if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                        visited[r][c] = True
                        heappush(heap, (grid[r][c], r, c))
            result[i] = point
        return result
