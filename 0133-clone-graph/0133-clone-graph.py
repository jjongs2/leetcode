"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        clones = {node: Node(node.val)}
        stack = [node]
        while stack:
            n0 = stack.pop()
            for n in n0.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)
                    stack.append(n)
                clones[n0].neighbors.append(clones[n])
        return clones[node]
