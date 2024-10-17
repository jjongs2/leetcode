class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_indices = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for larger in range(9, int(d), -1):
                j = last_indices.get(larger, -1)
                if i < j:
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num
