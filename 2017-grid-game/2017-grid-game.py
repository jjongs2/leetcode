class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_right = sum(grid[0]) - grid[0][0]
        bottom_left = 0
        result = max(top_right, bottom_left)
        for i in range(1, len(grid[0])):
            top_right -= grid[0][i]
            bottom_left += grid[1][i - 1]
            result = min(result, max(top_right, bottom_left))
        return result
