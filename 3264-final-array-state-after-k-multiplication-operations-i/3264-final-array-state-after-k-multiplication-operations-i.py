from heapq import heapify, heapreplace


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            _, i = heap[0]
            nums[i] *= multiplier
            heapreplace(heap, (nums[i], i))
        return nums
