from functools import reduce


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = reduce(lambda x, y: x | y, nums)

        def search(index, value):
            if value == max_value:
                return 1 << (n - index)
            if index == n:
                return 0
            return search(index + 1, value) + search(index + 1, value | nums[index])

        return search(0, 0)
