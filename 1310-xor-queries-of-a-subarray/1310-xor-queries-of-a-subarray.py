class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0 for _ in range(len(arr) + 1)]
        for i, num in enumerate(arr):
            prefix[i] = prefix[i - 1] ^ num
        return [prefix[right] ^ prefix[left - 1] for left, right in queries]
