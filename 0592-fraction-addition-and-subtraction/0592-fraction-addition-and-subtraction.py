from fractions import Fraction
from re import findall


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = (
            Fraction(int(a), int(b))
            for a, b in findall(r"([+-]?\d+)/(\d+)", expression)
        )
        result = sum(fractions)
        return f"{result.numerator}/{result.denominator}"
