class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        counts = dict()
        for row in matrix:
            if row[0] == 1:
                for c in range(n):
                    row[c] ^= 1
            key = tuple(row)
            counts[key] = counts.get(key, 0) + 1
        return max(counts.values())
