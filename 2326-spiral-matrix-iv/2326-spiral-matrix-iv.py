# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        top, left, bottom, right = 0, 0, m - 1, n - 1
        while True:
            for c in range(left, right + 1):
                matrix[top][c] = head.val
                if not (head := head.next):
                    return matrix
            top += 1
            for r in range(top, bottom + 1):
                matrix[r][right] = head.val
                if not (head := head.next):
                    return matrix
            right -= 1
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = head.val
                if not (head := head.next):
                    return matrix
            bottom -= 1
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = head.val
                if not (head := head.next):
                    return matrix
            left += 1
