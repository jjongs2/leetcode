class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        result = size = len(arr)
        indices = [0] * (size + 1)
        for i, num in enumerate(arr):
            indices[num] = i
        m, n = len(mat), len(mat[0])
        for r in range(m):
            row_max = 0
            for c in range(n):
                row_max = max(row_max, indices[mat[r][c]])
            result = min(result, row_max)
        for c in range(n):
            col_max = 0
            for r in range(m):
                col_max = max(col_max, indices[mat[r][c]])
            result = min(result, col_max)
        return result
