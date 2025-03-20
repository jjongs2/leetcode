class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        parents = list(range(n))
        costs = [-1] * n

        def find(v):
            while (p := parents[v]) != v:
                parents[v] = parents[p]
                v = parents[p]
            return v

        def union(v1, v2, w):
            p1, p2 = find(v1), find(v2)
            if p1 != p2:
                parents[p2] = p1
                costs[p1] &= costs[p2]
            costs[p1] &= w

        for v1, v2, w in edges:
            union(v1, v2, w)
        answer = [-1] * len(query)
        for i, (v1, v2) in enumerate(query):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                answer[i] = costs[p1]
        return answer
