class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        s = tuple(map(ord, str1))
        i = 0
        for c in map(ord, str2):
            while i < n and c - s[i] not in (-25, 0, 1):
                i += 1
            if i == n:
                return False
            i += 1
        return True
