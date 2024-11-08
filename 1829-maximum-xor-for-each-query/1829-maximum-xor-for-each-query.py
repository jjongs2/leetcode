class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        curr = 0
        result = []
        for num in nums:
            curr ^= num
            result.append(curr ^ mask)
        result.reverse()
        return result
