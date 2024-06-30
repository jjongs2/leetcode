class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.sizes = [1 for _ in range(n + 1)]

    def find(self, v):
        while (p := self.parents[v]) != v:
            self.parents[v] = self.parents[p]
            v = self.parents[v]
        return v

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        self.parents[p2] = p1
        self.sizes[p1] += self.sizes[p2]
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        alice, bob = UnionFind(n), UnionFind(n)
        for t, v1, v2 in edges:
            if t == 3 and alice.union(v1, v2):
                bob.union(v1, v2)
                count += 1
        for t, v1, v2 in edges:
            if t == 1 and alice.union(v1, v2):
                count += 1
            elif t == 2 and bob.union(v1, v2):
                count += 1
        alice_roots = set(alice.find(i) for i in range(1, n + 1))
        bob_roots = set(bob.find(i) for i in range(1, n + 1))
        if len(alice_roots) > 1 or len(bob_roots) > 1:
            return -1
        return len(edges) - count
