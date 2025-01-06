class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        for char in set(s):
            left, right = s.index(char), s.rindex(char)
            mids = {s[i] for i in range(left + 1, right)}
            count += len(mids)
        return count
