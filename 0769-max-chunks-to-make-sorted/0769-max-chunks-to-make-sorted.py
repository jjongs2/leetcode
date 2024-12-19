class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        max_val = 0
        for i, num in enumerate(arr):
            max_val = max(max_val, num)
            if max_val == i:
                count += 1
        return count
