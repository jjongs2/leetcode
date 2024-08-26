"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        visited = []
        stack = [root]
        while stack:
            node = stack.pop()
            visited.append(node.val)
            stack.extend(node.children)
        return visited[::-1]
