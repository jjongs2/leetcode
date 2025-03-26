from itertools import chain


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted(chain(*grid))
        median = nums[len(nums) // 2]
        remainder = median % x
        result = 0
        for num in nums:
            if num % x != remainder:
                return -1
            result += abs(num - median) // x
        return result
