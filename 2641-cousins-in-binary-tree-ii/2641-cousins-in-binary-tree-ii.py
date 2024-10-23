# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = deque([(root, None)])
        while q:
            level_sum = 0
            sibling_sums = defaultdict(int)
            for _ in range(len(q)):
                node, _ = q.popleft()
                for child in (node.left, node.right):
                    if not child:
                        continue
                    level_sum += child.val
                    sibling_sums[node] += child.val
                    q.append((child, node))
            for node, parent in q:
                node.val = level_sum - sibling_sums[parent]
        return root
