class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left, right = 0, s.count("1")
        for i in range(len(s) - 1):
            if s[i] == "0":
                left += 1
            else:
                right -= 1
            max_score = max(max_score, left + right)
        return max_score
