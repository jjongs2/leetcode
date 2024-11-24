from math import inf
from itertools import product


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        min_val = inf
        matrix_sum = minus_count = 0
        for r, c in product(range(n), repeat=2):
            if (num := matrix[r][c]) < 0:
                minus_count += 1
            abs_val = abs(num)
            matrix_sum += abs_val
            min_val = min(min_val, abs_val)
        if minus_count % 2 == 1:
            matrix_sum -= 2 * min_val
        return matrix_sum
