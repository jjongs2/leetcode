class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(num) % 2 == 0 for num in map(str, nums))
