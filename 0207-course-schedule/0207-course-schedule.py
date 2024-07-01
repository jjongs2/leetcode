from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegrees = defaultdict(int)
        for v1, v2 in prerequisites:
            adj[v2].append(v1)
            indegrees[v1] += 1
        to_visit = len(indegrees)
        stack = [v for v in adj.keys() if indegrees[v] == 0]
        while stack:
            v0 = stack.pop()
            for v in adj[v0]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    stack.append(v)
                    to_visit -= 1
        return to_visit == 0
