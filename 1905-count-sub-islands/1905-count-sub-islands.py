from itertools import product

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def is_subisland(r0, c0):
            result = 1
            grid2[r0][c0] = 0
            stack = [(r0, c0)]
            while stack:
                r0, c0 = stack.pop()
                result &= grid1[r0][c0]
                for dr, dc in DIRECTIONS:
                    r, c = r0 + dr, c0 + dc
                    if 0 <= r < m and 0 <= c < n and grid2[r][c] == 1:
                        grid2[r][c] = 0
                        stack.append((r, c))
            return result

        return sum(
            is_subisland(r, c)
            for r, c in product(range(m), range(n))
            if grid2[r][c] == 1
        )
