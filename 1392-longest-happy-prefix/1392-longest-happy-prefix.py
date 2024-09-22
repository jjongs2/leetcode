class Solution:
    def longestPrefix(self, s: str) -> str:
        s_len = len(s)
        lps = [0 for _ in range(s_len)]
        j = 0
        for i in range(1, s_len):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j
        return s[: lps[-1]]
