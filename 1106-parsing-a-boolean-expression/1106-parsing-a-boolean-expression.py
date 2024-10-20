OPERATORS = {"&": all, "|": any}
OPERANDS = {"t": True, "f": False}


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ",":
                continue
            if char in OPERANDS:
                stack.append(OPERANDS[char])
            elif char != ")":
                stack.append(char)
            else:
                operands = []
                while stack[-1] != "(":
                    operands.append(stack.pop())
                stack.pop()
                op = stack.pop()
                if op == "!":
                    stack.append(not operands[0])
                else:
                    stack.append(OPERATORS[op](operands))
        return stack[0]
