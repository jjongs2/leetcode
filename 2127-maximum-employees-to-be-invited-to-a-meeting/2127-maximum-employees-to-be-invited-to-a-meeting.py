from collections import deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        adj_lists = [set() for _ in range(n)]
        for v2, v1 in enumerate(favorite):
            adj_lists[v1].add(v2)
        visited = [False] * n

        def bfs(start):
            depth = 0
            visited[start] = True
            q = deque([start])
            while q:
                depth += 1
                for _ in range(len(q)):
                    v0 = q.popleft()
                    for v in adj_lists[v0]:
                        visited[v] = True
                        q.append(v)
            return depth

        result = 0
        cycle2_count = 0
        for v1 in favorite:
            if visited[v1]:
                continue
            v2 = favorite[v1]
            if v1 != favorite[v2]:
                continue
            adj_lists[v1].remove(v2)
            adj_lists[v2].remove(v1)
            result += bfs(v1) + bfs(v2)

        for v0 in range(n):
            if visited[v0]:
                continue
            path = set()
            v = v0
            while not visited[v]:
                visited[v] = True
                path.add(v)
                v = favorite[v]
            if v not in path:
                continue
            cycle_size = 1
            start = v
            while (v := favorite[v]) != start:
                cycle_size += 1
            result = max(result, cycle_size)
        return result
