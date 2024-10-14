from heapq import heapify, heapreplace


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        score = 0
        for _ in range(k):
            score -= heap[0]
            heapreplace(heap, heap[0] // 3)
        return score
