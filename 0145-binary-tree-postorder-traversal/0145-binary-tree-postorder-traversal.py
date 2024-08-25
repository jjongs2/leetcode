# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, visited = [], []
        last = None
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            top = stack[-1]
            if top.right and top.right != last:
                node = top.right
            else:
                last = stack.pop()
                visited.append(last.val)
        return visited
