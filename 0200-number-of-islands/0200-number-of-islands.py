from itertools import product


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((-1, 0), (0, -1), (0, 1), (1, 0))

        def search(r, c):
            stack = [(r, c)]
            while stack:
                r0, c0 = stack.pop()
                for dr, dc in directions:
                    r, c = r0 + dr, c0 + dc
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                        grid[r][c] = "0"
                        stack.append((r, c))

        count = 0
        m, n = len(grid), len(grid[0])
        for r, c in product(range(m), range(n)):
            if grid[r][c] == "1":
                grid[r][c] = "0"
                search(r, c)
                count += 1
        return count
