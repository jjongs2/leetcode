class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        freqs = [0] * 3
        result = 0
        l = 0
        for r in range(n):
            freqs[ord(s[r]) - ord("a")] += 1
            while freqs.count(0) == 0:
                result += n - r
                freqs[ord(s[l]) - ord("a")] -= 1
                l += 1
        return result
