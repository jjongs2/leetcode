from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = -1
        q = deque([root])
        while q:
            n = len(q)
            level += 1
            if level % 2 == 1:
                for i in range(n // 2):
                    j = n - 1 - i
                    q[i].val, q[j].val = q[j].val, q[i].val
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
        return root
