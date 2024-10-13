from heapq import heappop, heappush
from math import inf


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        iterators = tuple(map(iter, nums))
        max_value = -inf
        heap = []
        for index, iterator in enumerate(iterators):
            value = next(iterator)
            heappush(heap, (value, index))
            max_value = max(max_value, value)
        a, b = -inf, inf
        while True:
            min_value, index = heappop(heap)
            if max_value - min_value < b - a:
                a, b = min_value, max_value
            value = next(iterators[index], None)
            if value is None:
                break
            heappush(heap, (value, index))
            max_value = max(max_value, value)
        return [a, b]
