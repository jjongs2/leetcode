from itertools import product

OPERATORS = {"+", "-", "*"}


class Solution:
    def __init__(self):
        self.memo = dict()

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]
        if expression.isdigit():
            return [int(expression)]
        result = []
        for i, char in enumerate(expression):
            if char in OPERATORS:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1 :])
                for num1, num2 in product(left, right):
                    if char == "+":
                        result.append(num1 + num2)
                    elif char == "-":
                        result.append(num1 - num2)
                    elif char == "*":
                        result.append(num1 * num2)
        self.memo[expression] = result
        return result
