from sortedcontainers import SortedDict


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        sd = SortedDict({0: 0})
        for price, beauty in items:
            if beauty > sd.peekitem()[1]:
                sd[price] = beauty
        return [sd.peekitem(sd.bisect_right(query) - 1)[1] for query in queries]
