class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unclosed, unopened = 0, 0
        for char in s:
            if char == "(":
                unclosed += 1
            elif unclosed > 0:
                unclosed -= 1
            else:
                unopened += 1
        return unclosed + unopened
