from itertools import product

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def search(r0, c0, target):
            grid[r0][c0] = -target
            stack = [(r0, c0)]
            while stack:
                r0, c0 = stack.pop()
                for dr, dc in DIRECTIONS:
                    r, c = r0 + dr, c0 + dc
                    if not (0 <= r < m and 0 <= c < n):
                        continue
                    if grid[r][c] != target:
                        continue
                    grid[r][c] = -target
                    stack.append((r, c))

        island_count = 0
        lands = []
        for r, c in product(range(m), range(n)):
            if grid[r][c] == 0:
                continue
            lands.append((r, c))
            if grid[r][c] == 1:
                island_count += 1
                if island_count == 2:
                    return 0
                search(r, c, 1)
        if (land_count := len(lands)) <= 2:
            return land_count
        for r1, c1 in lands:
            island_count = 0
            target, grid[r1][c1] = grid[r1][c1], 0
            for r2, c2 in lands:
                if grid[r2][c2] == target:
                    island_count += 1
                    if island_count == 2:
                        return 1
                    search(r2, c2, target)
            grid[r1][c1] = -target
        return 2
