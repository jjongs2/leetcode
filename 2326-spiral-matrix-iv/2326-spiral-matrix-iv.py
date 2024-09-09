# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        r, c = 0, 0
        direction = 0
        dr, dc = DIRECTIONS[direction]
        while head:
            matrix[r][c] = head.val
            head = head.next
            r2, c2 = r + dr, c + dc
            if not (0 <= r2 < m and 0 <= c2 < n) or matrix[r2][c2] != -1:
                direction = (direction + 1) % 4
                dr, dc = DIRECTIONS[direction]
            r, c = r + dr, c + dc
        return matrix
