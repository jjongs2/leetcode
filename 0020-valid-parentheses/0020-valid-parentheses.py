OPEN_BRACKETS = {"(", "{", "["}
PAIRS = {")": "(", "}": "{", "]": "["}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in OPEN_BRACKETS:
                stack.append(char)
            elif stack and stack[-1] == PAIRS[char]:
                stack.pop()
            else:
                return False
        return not stack
