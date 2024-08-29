class MyDict(dict):
    def __missing__(self, key):
        return key


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = MyDict()

        def find(v):
            while (p := parents[v]) != v:
                parents[v] = parents[p]
                v = parents[p]
            return v

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            parents[p2] = p1

        for r, c in stones:
            union(r, ~c)
        return len(stones) - len({find(v) for v in parents})
