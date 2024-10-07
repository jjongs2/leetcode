class Solution:
    def minLength(self, s: str) -> int:
        pairs = {"B": "A", "D": "C"}
        stack = []
        for char in s:
            if char in pairs and stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
