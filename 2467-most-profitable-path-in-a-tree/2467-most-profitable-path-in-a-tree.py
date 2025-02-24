from collections import deque
from math import inf


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        n = len(amount)
        adj_lists = [[] for _ in range(n)]
        for a, b in edges:
            adj_lists[a].append(b)
            adj_lists[b].append(a)

        def find_bob_path():
            parents = [-1] * n
            parents[bob] = bob
            q = deque([bob])
            while True:
                v0 = q.popleft()
                for v in adj_lists[v0]:
                    if v == parents[v0]:
                        continue
                    parents[v] = v0
                    if v == 0:
                        path = deque([0])
                        while (v := parents[v]) != bob:
                            path.appendleft(v)
                        path.appendleft(bob)
                        return {v: i for i, v in enumerate(path)}
                    q.append(v)

        def find_max_income(bob_path):
            max_income = -inf
            parents = [-1] * n
            parents[0] = 0
            time = 0
            q = deque([(0, amount[0])])
            while q:
                time += 1
                for _ in range(len(q)):
                    v0, w0 = q.popleft()
                    for v in adj_lists[v0]:
                        if v == parents[v0]:
                            continue
                        parents[v] = v0
                        w = w0
                        if v not in bob_path or time < bob_path[v]:
                            w += amount[v]
                        elif time == bob_path[v]:
                            w += amount[v] // 2
                        if len(adj_lists[v]) == 1:
                            max_income = max(max_income, w)
                            continue
                        q.append((v, w))
            return max_income

        return find_max_income(find_bob_path())
