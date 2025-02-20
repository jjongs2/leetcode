class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        n = len(nums)
        for i in range(n):
            result.append("1" if nums[i][i] == "0" else "0")
        return "".join(result)
