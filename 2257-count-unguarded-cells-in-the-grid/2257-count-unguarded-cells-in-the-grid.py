from itertools import product


class Solution:
    DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [["B"] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = "G"
        for r, c in walls:
            grid[r][c] = "W"
        for r0, c0 in guards:
            for dr, dc in self.DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] not in "GW":
                    grid[r][c] = "X"
                    r, c = r + dr, c + dc
        return sum(grid[r][c] == "B" for r, c in product(range(m), range(n)))
