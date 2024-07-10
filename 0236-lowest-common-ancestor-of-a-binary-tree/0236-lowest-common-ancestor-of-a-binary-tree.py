# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        p_val, q_val = p.val, q.val

        def find_lca(node):
            if not node:
                return None
            if node.val in {p_val, q_val}:
                return node
            left = find_lca(node.left)
            right = find_lca(node.right)
            if left and right:
                return node
            return left or right

        return find_lca(root)
