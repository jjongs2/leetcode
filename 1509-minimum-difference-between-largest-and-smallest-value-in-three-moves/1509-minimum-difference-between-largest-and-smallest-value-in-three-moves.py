from heapq import nlargest
from heapq import nsmallest


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        largest = nlargest(4, nums)
        smallest = nsmallest(4, nums)
        return min(largest[i] - smallest[3 - i] for i in range(4))
