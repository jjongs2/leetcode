from collections import deque
from math import inf


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            max_val = -inf
            for _ in range(len(q)):
                node = q.popleft()
                max_val = max(max_val, node.val)
                for child in (node.left, node.right):
                    if child:
                        q.append(child)
            result.append(max_val)
        return result
