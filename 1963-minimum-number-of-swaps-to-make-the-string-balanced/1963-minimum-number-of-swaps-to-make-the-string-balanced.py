class Solution:
    def minSwaps(self, s: str) -> int:
        unbalance_count = 0
        for char in s:
            if char == "[":
                unbalance_count += 1
            elif unbalance_count > 0:
                unbalance_count -= 1
        return (unbalance_count + 1) // 2
