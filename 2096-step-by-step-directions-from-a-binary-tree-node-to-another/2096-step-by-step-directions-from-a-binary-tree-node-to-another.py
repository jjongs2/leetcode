# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def find_path(node, target, path=[]):
            if not node:
                return None
            if node.val == target:
                return path
            path.append("L")
            if find_path(node.left, target, path):
                return path
            path.pop()
            path.append("R")
            if find_path(node.right, target, path):
                return path
            path.pop()
            return None

        root_to_start = find_path(root, startValue, [])
        root_to_dest = find_path(root, destValue, [])
        i = 0
        bound = min(len(root_to_start), len(root_to_dest))
        while i < bound and root_to_start[i] == root_to_dest[i]:
            i += 1
        start_to_dest = ["U" for _ in range(len(root_to_start) - i)] + root_to_dest[i:]
        return "".join(start_to_dest)
