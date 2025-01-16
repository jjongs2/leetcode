class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = num1.bit_count() - num2.bit_count()
        x = num1
        mask = 1
        while n < 0:
            while x & mask == mask:
                mask <<= 1
            x |= mask
            n += 1
        mask = 1
        while n > 0:
            while x & mask == 0:
                mask <<= 1
            x ^= mask
            n -= 1
        return x
