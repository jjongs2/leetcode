class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = {int(num, base=2) for num in nums}
        for num in range(1 << n):
            if num not in nums_set:
                return f"{num:0{n}b}"
