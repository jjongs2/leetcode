class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {num: rank for rank, num in enumerate(sorted(set(arr)), start=1)}
        return [ranks[num] for num in arr]
