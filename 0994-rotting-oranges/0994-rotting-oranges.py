from collections import deque
from itertools import product


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        for r, c in product(range(m), range(n)):
            cell = grid[r][c]
            if cell == 1:
                fresh_count += 1
            elif cell == 2:
                queue.append((r, c))
        minute = 0
        while queue:
            if fresh_count == 0:
                break
            for _ in range(len(queue)):
                r0, c0 = queue.popleft()
                for dr, dc in directions:
                    r, c = r0 + dr, c0 + dc
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh_count -= 1
            minute += 1
        return minute if fresh_count == 0 else -1
