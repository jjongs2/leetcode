class Solution:
    def minSwaps(self, s: str) -> int:
        open_count = 0
        unbalance_count = 0
        for char in s:
            if char == "[":
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                unbalance_count += 1
        return (unbalance_count + 1) // 2
