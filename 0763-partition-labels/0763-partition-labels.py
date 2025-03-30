class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        seen = {c: i for i, c in enumerate(s)}
        n = len(s)
        start = 0
        while start < n:
            end = seen[s[start]]
            i = start + 1
            while i < end:
                end = max(end, seen[s[i]])
                i += 1
            result.append(end - start + 1)
            start = end + 1
        return result
