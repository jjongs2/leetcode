# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        def search(node):
            if not node:
                return []
            if not (node.left or node.right):
                return [1]
            left = search(node.left)
            right = search(node.right)
            self.count += sum(l + r <= distance for l in left for r in right)
            return [d + 1 for d in left + right if d + 1 < distance]

        search(root)
        return self.count
