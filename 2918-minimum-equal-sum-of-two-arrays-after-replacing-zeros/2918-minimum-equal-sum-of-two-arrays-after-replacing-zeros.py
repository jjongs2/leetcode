class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1, s1 = self._helper(nums1)
        z2, s2 = self._helper(nums2)
        if z1 == 0 and s1 < s2 + z2:
            return -1
        if z2 == 0 and s2 < s1 + z1:
            return -1
        return max(s1 + z1, s2 + z2)

    @staticmethod
    def _helper(nums):
        zero_count, total_sum = 0, 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_sum += num
        return zero_count, total_sum
