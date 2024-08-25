VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        prev = 0
        for char in s:
            curr = VALUES[char]
            if curr > prev:
                curr -= prev * 2
            result += curr
            prev = curr
        return result
