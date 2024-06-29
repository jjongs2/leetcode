from operator import add
from operator import sub
from operator import mul


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y)
        }
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(operators[token](n1, n2))
        return stack[0]
