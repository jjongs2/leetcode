from collections import deque
from itertools import product


class Solution:
    DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        q = deque()
        for r, c in product(range(m), range(n)):
            if isWater[r][c]:
                q.append((r, c))
                heights[r][c] = 0
        while q:
            r0, c0 = q.popleft()
            for dr, dc in self.DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if not (0 <= r < m and 0 <= c < n):
                    continue
                if heights[r][c] != -1:
                    continue
                heights[r][c] = heights[r0][c0] + 1
                q.append((r, c))
        return heights
