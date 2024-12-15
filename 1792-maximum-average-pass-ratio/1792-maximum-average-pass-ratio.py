from heapq import heapify, heapreplace


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
        heapify(heap)
        for _ in range(extraStudents):
            _, a, b = heap[0]
            a, b = a + 1, b + 1
            heapreplace(heap, (a / b - (a + 1) / (b + 1), a, b))
        return sum(a / b for _, a, b in heap) / len(heap)
