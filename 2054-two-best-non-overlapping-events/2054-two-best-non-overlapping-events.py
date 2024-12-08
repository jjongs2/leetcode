from bisect import bisect_left


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        result = 0
        max_ends, max_values = [0], [0]
        events.sort(key=lambda x: x[1])
        for s, e, v in events:
            i = bisect_left(max_ends, s) - 1
            result = max(result, max_values[i] + v)
            if v > max_values[-1]:
                max_ends.append(e)
                max_values.append(v)
        return result
