DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        path = [[rStart, cStart]]
        r, c = rStart, cStart
        i = 0
        size = rows * cols
        while len(path) < size:
            dr, dc = DIRECTIONS[i % 4]
            for _ in range(i // 2 + 1):
                r, c = r + dr, c + dc
                if 0 <= r < rows and 0 <= c < cols:
                    path.append([r, c])
            i += 1
        return path
