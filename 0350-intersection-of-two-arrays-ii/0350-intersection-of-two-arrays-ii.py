from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        return [n for n in c1 if n in c2 for _ in range(min(c1[n], c2[n]))]
