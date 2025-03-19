class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        bits = 0b111
        for num in nums:
            bits = ((bits << 1) | num) & 0b111
            if bits & 0b100 == 0:
                bits ^= 0b111
                count += 1
        return count if bits == 0b111 else -1
