from itertools import chain


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        if m <= 1 or n <= 1:
            return [*chain.from_iterable(matrix)]
        return (
            matrix[0][:-1]
            + [matrix[r][-1] for r in range(m - 1)]
            + [matrix[-1][c] for c in range(n - 1, 0, -1)]
            + [matrix[r][0] for r in range(m - 1, 0, -1)]
            + self.spiralOrder([row[1 : n - 1] for row in matrix[1 : m - 1]])
        )
