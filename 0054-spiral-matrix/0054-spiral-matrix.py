class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                visited.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):
                visited.append(matrix[r][right])
            right -= 1
            if top > bottom or left > right:
                break
            for c in range(right, left - 1, -1):
                visited.append(matrix[bottom][c])
            bottom -= 1
            for r in range(bottom, top - 1, -1):
                visited.append(matrix[r][left])
            left += 1
        return visited
