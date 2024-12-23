from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        count = 0
        q = deque([root])
        while q:
            n = len(q)
            vals = [node.val for node in q]
            sorted_vals = sorted(vals)
            indices = {val: idx for idx, val in enumerate(vals)}
            for i in range(n):
                if vals[i] == sorted_vals[i]:
                    continue
                v, sv = vals[i], sorted_vals[i]
                vals[i], vals[indices[sv]] = sv, v
                indices[v], indices[sv] = indices[sv], indices[v]
                count += 1
            for _ in range(n):
                node = q.popleft()
                for child in (node.left, node.right):
                    if child:
                        q.append(child)
        return count
