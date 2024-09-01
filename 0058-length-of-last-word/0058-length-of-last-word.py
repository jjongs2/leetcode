class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in reversed(s):
            if char != ' ':
                length += 1
            elif length > 0:
                break
        return length