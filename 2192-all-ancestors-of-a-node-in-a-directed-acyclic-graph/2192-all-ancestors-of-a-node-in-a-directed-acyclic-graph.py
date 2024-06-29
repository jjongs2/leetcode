from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for _ in range(n)]
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            ancestors[v2].add(v1)
        q = deque()
        indegrees = [len(preds) for preds in ancestors]
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)
        while q:
            v0 = q.popleft()
            for v in adj[v0]:
                ancestors[v] |= ancestors[v0]
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        return [sorted(ancestor) for ancestor in ancestors]
