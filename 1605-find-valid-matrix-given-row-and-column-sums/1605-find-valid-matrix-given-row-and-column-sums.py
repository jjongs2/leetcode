class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = []
        row_count, col_count = len(rowSum), len(colSum)
        for r in range(row_count):
            row = []
            for c in range(col_count):
                element = min(rowSum[r], colSum[c])
                row.append(element)
                rowSum[r] -= element
                colSum[c] -= element
            matrix.append(row)
        return matrix
