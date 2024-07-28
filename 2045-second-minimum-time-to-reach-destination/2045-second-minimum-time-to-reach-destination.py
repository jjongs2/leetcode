from collections import deque

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        def search(start, end):
            visited = [set() for _ in range(n + 1)]
            visited[start].add(0)
            length = 0
            q = deque([start])
            while q:
                length += 1
                for _ in range(len(q)):
                    v0 = q.popleft()
                    for v in adj[v0]:
                        if len(visited[v]) == 2:
                            continue
                        visited[v].add(length)
                        if len(visited[end]) == 2:
                            return max(visited[end])
                        q.append(v)
        
        length = search(1, n)
        curr_time = 0
        while length > 1:
            curr_time += time
            quotient = curr_time // change
            if quotient % 2 == 1:
                curr_time = change * (quotient + 1)
            length -= 1
        return curr_time + time
