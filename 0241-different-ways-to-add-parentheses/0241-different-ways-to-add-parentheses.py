from itertools import product


class Solution:
    def __init__(self):
        self.memo = {str(num): [num] for num in range(100)}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]
        result = []
        for i, char in enumerate(expression):
            if char.isdigit():
                continue
            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i + 1 :])
            for lhs, rhs in product(left, right):
                if char == "+":
                    result.append(lhs + rhs)
                elif char == "-":
                    result.append(lhs - rhs)
                elif char == "*":
                    result.append(lhs * rhs)
        self.memo[expression] = result
        return result
