class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for x in arr1:
            if x in prefixes:
                continue
            while x > 0:
                prefixes.add(x)
                x //= 10
        max_num = 0
        for y in set(arr2):
            while y > 0:
                if y in prefixes:
                    max_num = max(max_num, y)
                    break
                y //= 10
        return len(str(max_num)) if max_num > 0 else 0
