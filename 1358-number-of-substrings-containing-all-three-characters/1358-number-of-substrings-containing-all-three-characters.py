class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        last_i = [-1] * 3
        for i, char in enumerate(s):
            last_i[ord(char) - ord('a')] = i
            result += min(last_i) + 1
        return result
