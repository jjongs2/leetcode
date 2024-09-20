class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        s_reverse = s[::-1]
        w = s + " " + s_reverse
        w_len = len(w)
        lps = [0 for _ in range(w_len)]
        j = 0
        for i in range(1, w_len):
            while j > 0 and w[i] != w[j]:
                j = lps[j - 1]
            if w[i] == w[j]:
                j += 1
                lps[i] = j
        return s_reverse[: -lps[-1]] + s
