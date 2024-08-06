from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        adj = [set() for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].add(v2)
            adj[v2].add(v1)
        leaves = [v for v in range(n) if len(adj[v]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                parent = adj[leaf].pop()
                adj[parent].remove(leaf)
                if len(adj[parent]) == 1:
                    new_leaves.append(parent)
            leaves = new_leaves
        return leaves
