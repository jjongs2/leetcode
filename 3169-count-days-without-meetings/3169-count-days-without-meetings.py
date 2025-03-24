from collections import defaultdict


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        diff = defaultdict(int)
        for start, end in meetings:
            diff[start - 1] += 1
            diff[end] -= 1
        diff[days] = 0
        result = 0
        meeting = 0
        prev = 0
        for curr in sorted(diff):
            if meeting == 0:
                result += curr - prev
            meeting += diff[curr]
            prev = curr
        return result
