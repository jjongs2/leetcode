class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1 or k == 1:
            return "0"
        if k.bit_count() == 1:
            return "1"
        if k > (1 << n - 1):
            return "1" if self.findKthBit(n - 1, (1 << n) - k) == "0" else "0"
        return self.findKthBit(n - 1, k)
