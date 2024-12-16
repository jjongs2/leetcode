from heapq import heapify, heapreplace


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            num, i = heap[0]
            heapreplace(heap, (num * multiplier, i))
        heap.sort(key=lambda x: x[1])
        return [num for num, _ in heap]
