# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, visited):
            if not node:
                return
            inorder(node.left, visited)
            visited.append(node.val)
            inorder(node.right, visited)

        def make_bst(start, end):
            if start >= end:
                return None
            mid = (start + end) // 2
            return TreeNode(nums[mid], make_bst(start, mid), make_bst(mid + 1, end))

        nums = []
        inorder(root, nums)
        return make_bst(0, len(nums))
