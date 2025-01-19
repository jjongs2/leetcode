from heapq import heapify, heappop, heappush
from itertools import product


class Solution:
    DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        visited = [[False] * n for _ in range(m)]
        heap = []
        for r, c in product((0, m - 1), range(n)):
            heap.append((heightMap[r][c], r, c))
            visited[r][c] = True
        for r, c in product(range(1, m - 1), (0, n - 1)):
            heap.append((heightMap[r][c], r, c))
            visited[r][c] = True
        heapify(heap)
        water = 0
        max_h = 0
        while heap:
            h0, r0, c0 = heappop(heap)
            max_h = max(max_h, h0)
            for dr, dc in self.DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if not (0 <= r < m and 0 <= c < n):
                    continue
                if visited[r][c]:
                    continue
                visited[r][c] = True
                h = heightMap[r][c]
                water += max(0, max_h - h)
                heappush(heap, (h, r, c))
        return water
