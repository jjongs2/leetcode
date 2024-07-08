class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        for divisor in range(2, n + 1):
            index = (index + k) % divisor
        return index + 1
