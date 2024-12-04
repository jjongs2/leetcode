class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str2)
        i = 0
        for c in str1:
            if (ord(str2[i]) - ord(c)) % 26 <= 1:
                i += 1
                if i == n:
                    return True
        return False
