from itertools import product

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = 4 * n * n
        parents = list(range(size))

        def find(v):
            while (p := parents[v]) != v:
                parents[v] = parents[p]
                v = parents[p]
            return v

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            parents[p2] = p1

        def index(r, c, direction):
            return 4 * (r * n + c) + direction

        for r, c in product(range(n), repeat=2):
            if r > 0:
                union(index(r - 1, c, BOTTOM), index(r, c, TOP))
            if c > 0:
                union(index(r, c - 1, RIGHT), index(r, c, LEFT))
            if grid[r][c] != "/":
                union(index(r, c, TOP), index(r, c, RIGHT))
                union(index(r, c, BOTTOM), index(r, c, LEFT))
            if grid[r][c] != "\\":
                union(index(r, c, TOP), index(r, c, LEFT))
                union(index(r, c, BOTTOM), index(r, c, RIGHT))
        return len(set(find(v) for v in range(size)))
