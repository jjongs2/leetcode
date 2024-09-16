VOWELS = "aeiou"


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        max_length = 0
        memo = {0: -1}
        bits = 0
        mask = {v: 1 << i for i, v in enumerate(VOWELS)}
        for i, char in enumerate(s):
            if char in mask:
                bits ^= mask[char]
            if bits in memo:
                max_length = max(max_length, i - memo[bits])
            else:
                memo[bits] = i
        return max_length
