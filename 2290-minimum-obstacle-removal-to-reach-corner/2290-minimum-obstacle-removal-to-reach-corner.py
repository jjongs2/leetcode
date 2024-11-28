from collections import deque
from math import inf


class Solution:
    DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[inf] * n for _ in range(m)]
        visited[0][0] = 0
        q = deque([(0, 0)])
        while q:
            r0, c0 = q.popleft()
            v0 = visited[r0][c0]
            for dr, dc in self.DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if not (0 <= r < m and 0 <= c < n):
                    continue
                w = grid[r][c]
                v = v0 + w
                if v >= visited[r][c]:
                    continue
                visited[r][c] = v
                if w == 0:
                    q.appendleft((r, c))
                else:
                    q.append((r, c))
        return visited[-1][-1]
