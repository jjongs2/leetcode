class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        self.count = 0
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(v, p):
            value = values[v] + sum(dfs(child, v) for child in adj[v] if child != p)
            if value % k == 0:
                self.count += 1
                return 0
            return value

        dfs(0, -1)
        return self.count
