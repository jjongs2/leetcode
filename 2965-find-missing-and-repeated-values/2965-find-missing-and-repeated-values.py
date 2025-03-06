class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = set(range(1, n * n + 1))
        a = 0
        for row in grid:
            for x in row:
                if x in nums:
                    nums.remove(x)
                else:
                    a = x
        b = nums.pop()
        return [a, b]
