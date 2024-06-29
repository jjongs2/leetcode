class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v2].append(v1)
        answer = [[] for _ in range(n)]
        for i in range(n):
            stack = [i]
            visited = set()
            while stack:
                v0 = stack.pop()
                for v in adj[v0]:
                    if v in visited:
                        continue
                    stack.append(v)
                    visited.add(v)
            answer[i] = sorted(visited)
        return answer
