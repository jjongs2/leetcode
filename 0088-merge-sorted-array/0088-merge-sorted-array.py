class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                n -= 1
                nums1[m + n] = nums2[n]
            else:
                m -= 1
                nums1[m + n] = nums1[m]
        nums1[:n] = nums2[:n]
