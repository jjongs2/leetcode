class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1, set2 = set(map(str, arr1)), set(map(str, arr2))
        prefixes = set(x[:i] for x in set1 for i in range(len(x), 0, -1))
        max_len = 0
        for y in set2:
            for i in range(len(y), 0, -1):
                prefix = y[:i]
                if prefix in prefixes:
                    max_len = max(max_len, len(prefix))
                    break
        return max_len
