class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        sorted_intervals = sorted(intervals)
        curr_start, curr_end = sorted_intervals[0]
        for start, end in sorted_intervals:
            if start <= curr_end:
                curr_end = max(curr_end, end)
                continue
            result.append([curr_start, curr_end])
            curr_start, curr_end = start, end
        result.append([curr_start, curr_end])
        return result
