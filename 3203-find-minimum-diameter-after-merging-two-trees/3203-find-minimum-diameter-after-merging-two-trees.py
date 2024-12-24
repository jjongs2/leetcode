from collections import deque


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        d1 = self._find_diameter(edges1)
        d2 = self._find_diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)

    @staticmethod
    def _find_diameter(edges):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def bfs(start):
            depth = -1
            node = -1
            visited = [False] * n
            visited[start] = True
            q = deque([start])
            while q:
                depth += 1
                for _ in range(len(q)):
                    node = q.popleft()
                    for next_node in adj[node]:
                        if visited[next_node]:
                            continue
                        visited[next_node] = True
                        q.append(next_node)
            return depth, node

        _, leaf = bfs(0)
        diameter, _ = bfs(leaf)
        return diameter
