from heapq import heappop, heappush


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = [[] for _ in range(n)]
        for (v1, v2), prob in zip(edges, succProb):
            adj[v1].append((v2, prob))
            adj[v2].append((v1, prob))
        probs = [0.0 for _ in range(n)]
        probs[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            prob1, v1 = heappop(heap)
            prob1 *= -1.0
            if v1 == end_node:
                break
            if prob1 < probs[v1]:
                continue
            for v2, prob2 in adj[v1]:
                prob2 *= prob1
                if prob2 > probs[v2]:
                    probs[v2] = prob2
                    heappush(heap, (-prob2, v2))
        return probs[end_node]
