# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(start_p, start_i, end_i):
            if start_i == end_i:
                return None
            root_val = preorder[start_p]
            root_i = inorder.index(root_val, start_i, end_i)
            return TreeNode(
                root_val,
                construct(start_p + 1, start_i, root_i),
                construct(start_p + root_i - start_i + 1, root_i + 1, end_i),
            )

        return construct(0, 0, len(inorder))
