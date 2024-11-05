from heapq import heappush, heappop
from math import inf


class MedianFinder:
    def __init__(self):
        self.min_heap = [inf]
        self.max_heap = [inf]

    def addNum(self, num: int) -> None:
        if num > self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
        min_size, max_size = len(self.min_heap), len(self.max_heap)
        if min_size - max_size > 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        elif max_size - min_size > 1:
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        min_size, max_size = len(self.min_heap), len(self.max_heap)
        if min_size < max_size:
            return -self.max_heap[0]
        if min_size > max_size:
            return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
