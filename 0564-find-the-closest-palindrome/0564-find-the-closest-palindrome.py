class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        half = (length + 1) // 2
        is_even = length % 2 == 0
        num, num_left = int(n), int(n[:half])
        palindromes = {10 ** (length - 1) - 1, 10**length + 1}
        for i in (-1, 0, 1):
            left = str(num_left + i)
            if len(left) == half:
                right = left[::-1] if is_even else left[-2::-1]
                palindromes.add(int(left + right))
        palindromes.discard(num)
        return str(min(palindromes, key=lambda x: (abs(x - num), x)))
