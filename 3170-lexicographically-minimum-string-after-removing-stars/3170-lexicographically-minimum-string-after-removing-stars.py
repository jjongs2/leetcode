from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def clearStars(self, s: str) -> str:
        freqs = defaultdict(int)
        heap = []
        for i, char in enumerate(s):
            if char == "*":
                heappop(heap)
            else:
                freqs[char] += 1
                heappush(heap, (char, -freqs[char], i))
        heap.sort(key=lambda x: x[2])
        return "".join(x[0] for x in heap)
