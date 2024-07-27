from itertools import product
from math import inf


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        ORD_a = ord("a")
        SIZE = 26

        def index(char):
            return ord(char) - ORD_a

        costs = [[inf for _ in range(SIZE)] for _ in range(SIZE)]
        from_map, to_map = map(index, original), map(index, changed)
        from_set, to_set = set(), set()
        for v1, v2, weight in zip(from_map, to_map, cost):
            costs[v1][v2] = min(costs[v1][v2], weight)
            from_set.add(v1)
            to_set.add(v2)
        for via, v1, v2 in product(from_set & to_set, from_set, to_set):
            costs[v1][v2] = min(costs[v1][v2], costs[v1][via] + costs[via][v2])
        total_cost = 0
        for c1, c2 in zip(source, target):
            if c1 == c2:
                continue
            v1, v2 = index(c1), index(c2)
            if (weight := costs[v1][v2]) == inf:
                return -1
            total_cost += weight
        return total_cost
