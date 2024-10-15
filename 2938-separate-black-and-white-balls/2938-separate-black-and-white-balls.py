class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        ones = 0
        for char in s:
            if char == "1":
                ones += 1
            else:
                steps += ones
        return steps
