class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ")":
                stack.append(char)
                continue
            substr = []
            while stack[-1] != "(":
                substr.append(stack.pop())
            stack.pop()
            stack.extend(substr)
        return "".join(stack)
