class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for start, end in sorted(intervals):
            if not result or result[-1][1] < start:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)
        return result
