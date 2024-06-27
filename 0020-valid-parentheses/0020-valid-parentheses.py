class Solution:
    PAIRS = {")": "(", "}": "{", "]": "["}

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char not in self.PAIRS:
                stack.append(char)
            elif stack and stack[-1] == self.PAIRS[char]:
                stack.pop()
            else:
                return False
        return not stack
