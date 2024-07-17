# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        trees = []
        targets = set(to_delete)

        def delete_targets(node, is_root):
            if not node:
                return None
            is_target = node.val in targets
            if is_root and not is_target:
                trees.append(node)
            node.left = delete_targets(node.left, is_target)
            node.right = delete_targets(node.right, is_target)
            return node if not is_target else None

        delete_targets(root, True)
        return trees
