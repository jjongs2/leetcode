from math import inf
from sortedcontainers import SortedDict


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        max_to, max_from = dict(), SortedDict({inf: 0})
        max_v = 0
        events.sort(key=lambda x: x[1])
        for _, e, v in events:
            max_v = max(max_v, v)
            max_to[e] = max_v
        max_v = 0
        events.sort(reverse=True)
        for s, _, v in events:
            max_v = max(max_v, v)
            max_from[s] = max_v
        result = 0
        for e, v1 in max_to.items():
            _, v2 = max_from.peekitem(max_from.bisect_right(e))
            result = max(result, v1 + v2)
        return result
