from collections import defaultdict
from itertools import product


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = defaultdict(list, {c: [[c]] for c in candidates if c <= target})
        for i, c in product(range(4, target + 1), candidates):
            if i - c < 2:
                continue
            for combination in combinations[i - c]:
                if c >= combination[-1]:
                    combinations[i].append(combination + [c])
        return combinations[target]
