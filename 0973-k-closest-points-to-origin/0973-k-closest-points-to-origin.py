from heapq import heappush
from heapq import heappushpop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            d = x**2 + y**2
            if len(heap) < k:
                heappush(heap, (-d, [x, y]))
            else:
                heappushpop(heap, (-d, [x, y]))
        return [point for _, point in heap]
