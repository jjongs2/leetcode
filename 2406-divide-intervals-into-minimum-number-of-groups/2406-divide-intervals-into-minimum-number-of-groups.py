from heapq import heappush, heapreplace


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        for left, right in sorted(intervals):
            if heap and heap[0] < left:
                heapreplace(heap, right)
            else:
                heappush(heap, right)
        return len(heap)
