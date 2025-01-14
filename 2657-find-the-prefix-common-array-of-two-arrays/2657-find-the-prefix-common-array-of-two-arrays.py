class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        bits_a = bits_b = 0
        result = [0] * len(A)
        for i, (a, b) in enumerate(zip(A, B)):
            bits_a |= 1 << a
            bits_b |= 1 << b
            result[i] = (bits_a & bits_b).bit_count()
        return result
