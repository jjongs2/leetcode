from itertools import product


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        pos = [None] * (m * n + 1)
        for r, c in product(range(m), range(n)):
            pos[mat[r][c]] = (r, c)
        row_counts = [0] * m
        col_counts = [0] * n
        for i, num in enumerate(arr):
            r, c = pos[num]
            row_counts[r] += 1
            col_counts[c] += 1
            if row_counts[r] == n or col_counts[c] == m:
                return i
