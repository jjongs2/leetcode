from fractions import Fraction
from re import findall


class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = sum(map(Fraction, findall(r"[+-]?\d+/\d+", expression)))
        return f"{result.numerator}/{result.denominator}"
