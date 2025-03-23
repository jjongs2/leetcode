from heapq import heappop, heappush


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_lists = [[] for _ in range(n)]
        for v1, v2, w in roads:
            adj_lists[v1].append((v2, w))
            adj_lists[v2].append((v1, w))
        counts = [1] * n
        visited = [inf] * n
        visited[0] = 0
        heap = [(0, 0)]
        while heap:
            w0, v0 = heappop(heap)
            if w0 > visited[v0]:
                continue
            for v, dw in adj_lists[v0]:
                w = w0 + dw
                if w == visited[v]:
                    counts[v] += counts[v0]
                elif w < visited[v]:
                    visited[v] = w
                    counts[v] = counts[v0]
                    heappush(heap, (w, v))
        return counts[-1] % (10**9 + 7)
