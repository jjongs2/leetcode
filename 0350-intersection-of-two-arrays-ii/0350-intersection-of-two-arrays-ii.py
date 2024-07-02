from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        counter = Counter(nums1)
        for num in nums2:
            if counter[num] > 0:
                counter[num] -= 1
                result.append(num)
        return result
