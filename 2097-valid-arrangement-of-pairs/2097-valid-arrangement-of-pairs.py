from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        for start, end in pairs:
            adj[start].append(end)
            outdeg[start] += 1
            indeg[end] += 1
        start = pairs[0][0]
        for v in adj:
            if outdeg[v] - indeg[v] == 1:
                start = v
                break
        path = []
        stack = [start]
        while stack:
            v0 = stack[-1]
            if adj[v0]:
                stack.append(adj[v0].pop())
            else:
                path.append(stack.pop())
        path.reverse()
        return [[path[i - 1], path[i]] for i in range(1, len(path))]
