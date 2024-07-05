from math import inf


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(low, node, high):
            if not node:
                return True
            val = node.val
            if not (low < val < high):
                return False
            return validate(low, node.left, val) and validate(val, node.right, high)

        return validate(-inf, root, inf)
