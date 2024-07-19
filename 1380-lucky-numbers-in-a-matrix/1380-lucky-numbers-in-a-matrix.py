class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = set(map(min, matrix))
        for col in zip(*matrix):
            col_max = max(col)
            if col_max in row_mins:
                return [col_max]
        return []
