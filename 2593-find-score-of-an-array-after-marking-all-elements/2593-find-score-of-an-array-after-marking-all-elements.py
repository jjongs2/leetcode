from heapq import heapify, heappop


class Solution:
    def findScore(self, nums: List[int]) -> int:
        is_marked = [False] * (len(nums) + 1)
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)
        score = 0
        while heap:
            num, i = heappop(heap)
            if is_marked[i]:
                continue
            is_marked[i] = is_marked[i - 1] = is_marked[i + 1] = True
            score += num
        return score
