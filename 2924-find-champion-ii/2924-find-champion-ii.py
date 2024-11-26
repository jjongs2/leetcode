class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champions = set(range(n))
        for _, v in edges:
            champions.discard(v)
        return next(iter(champions)) if len(champions) == 1 else -1
