class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = (time // (n - 1)) & 1
        index = time % (n - 1)
        return index + 1 if direction == 0 else n - index
