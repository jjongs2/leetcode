from collections import deque


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        adj = [[i] for i in range(1, n + 1)]

        def bfs(start=0, end=n - 1):
            depth = 0
            q = deque([start])
            visited = [False] * n
            while q:
                depth += 1
                for _ in range(len(q)):
                    v0 = q.popleft()
                    for v in adj[v0]:
                        if visited[v]:
                            continue
                        if v == end:
                            return depth
                        visited[v] = True
                        q.append(v)

        result = []
        for v1, v2 in queries:
            adj[v1].append(v2)
            result.append(bfs())
        return result
