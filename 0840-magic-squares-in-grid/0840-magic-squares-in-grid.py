class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(r0, c0):
            nums = {grid[r][c] for r in range(r0, r0 + 3) for c in range(c0, c0 + 3)}
            if nums != set(range(1, 10)):
                return False
            for r in range(r0, r0 + 3):
                if sum(grid[r][c0 : c0 + 3]) != 15:
                    return False
            for c in range(c0, c0 + 3):
                if sum(grid[r][c] for r in range(r0, r0 + 3)) != 15:
                    return False
            if sum(grid[r0 + i][c0 + i] for i in range(3)) != 15:
                return False
            if sum(grid[r0 + i][c0 + 2 - i] for i in range(3)) != 15:
                return False
            return True

        m, n = len(grid), len(grid[0])
        return sum(is_magic_square(r, c) for r in range(m - 2) for c in range(n - 2))
