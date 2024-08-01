from itertools import product

TO_LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapped = (TO_LETTERS[d] for d in digits)
        return ["".join(p) for p in product(*mapped)]
