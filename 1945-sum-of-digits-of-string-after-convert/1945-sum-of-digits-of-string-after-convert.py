ord_a = ord("a")


def transform(char):
    index = ord(char) - ord_a + 1
    return index // 10 + index % 10


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = sum(transform(char) for char in s)
        for _ in range(k - 1):
            num = sum(int(digit) for digit in str(num))
        return num
