from collections import Counter
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        counter = Counter(nums)
        for n1, n2 in combinations(counter.keys(), 2):
            n3 = -(n1 + n2)
            if n1 < n3 and n2 < n3 and n3 in counter:
                triplets.append([n1, n2, n3])
        if counter.get(0, 0) >= 3:
            triplets.append([0, 0, 0])
        del counter[0]
        for n, count in counter.items():
            if count >= 2 and -2 * n in counter:
                triplets.append([n, n, -2 * n])
        return triplets
