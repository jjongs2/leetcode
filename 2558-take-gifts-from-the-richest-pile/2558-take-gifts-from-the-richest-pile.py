from heapq import heapify, heapreplace
from math import isqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapify(heap)
        for _ in range(k):
            heapreplace(heap, -isqrt(-heap[0]))
        return -sum(heap)
