from itertools import product
from math import inf


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        distances = [[inf for _ in range(n)] for _ in range(n)]
        for v1, v2, weight in edges:
            distances[v1][v2] = weight
            distances[v2][v1] = weight
        for via, v1, v2 in product(range(n), repeat=3):
            if v1 == v2:
                continue
            distances[v1][v2] = min(
                distances[v1][v2], distances[v1][via] + distances[via][v2]
            )
        counts = [sum(d <= distanceThreshold for d in distances[v]) for v in range(n)]
        return min(enumerate(counts), key=lambda x: (x[1], -x[0]))[0]
