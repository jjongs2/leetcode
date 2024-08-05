from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for string, count in Counter(arr).items():
            if count > 1:
                continue
            k -= 1
            if k == 0:
                return string
        return ""
