class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_lists = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj_lists[v1].append(v2)
            adj_lists[v2].append(v1)
        count = 0
        visited = [False] * n
        for v0 in range(n):
            if visited[v0]:
                continue
            visited[v0] = True
            path = [v0]
            stack = [v0]
            while stack:
                v1 = stack.pop()
                for v2 in adj_lists[v1]:
                    if visited[v2]:
                        continue
                    visited[v2] = True
                    stack.append(v2)
                    path.append(v2)
            k = len(path)
            if all(len(adj_lists[v]) == k - 1 for v in path):
                count += 1
        return count
