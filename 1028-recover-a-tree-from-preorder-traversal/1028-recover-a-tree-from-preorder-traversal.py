# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        traversal += "-"
        dummy = TreeNode()
        stack = [(-1, dummy)]
        j = 0
        while j < n:
            i = j
            while traversal[j] == "-":
                j += 1
            depth = j - i
            i = j
            while traversal[j] != "-":
                j += 1
            node = TreeNode(int(traversal[i:j]))
            while depth <= stack[-1][0]:
                stack.pop()
            parent = stack[-1][1]
            if parent.left:
                parent.right = node
            else:
                parent.left = node
            stack.append((depth, node))
        return dummy.left
