class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        new_start, new_end = newInterval
        for i, (start, end) in enumerate(intervals):
            if end < new_start:
                result.append([start, end])
            elif new_end < start:
                result.append([new_start, new_end])
                return result + intervals[i:]
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        result.append([new_start, new_end])
        return result
