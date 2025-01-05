class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        changes = [0] * (n + 1)
        for start, end, direction in shifts:
            change = 1 if direction == 1 else -1
            changes[start] += change
            changes[end + 1] -= change
        for i in range(1, n):
            changes[i] += changes[i - 1]
        a = ord("a")
        return "".join(
            chr((ord(char) - a + change) % 26 + a) for char, change in zip(s, changes)
        )
