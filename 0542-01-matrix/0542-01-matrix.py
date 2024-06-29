from collections import deque
from itertools import product


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        deq = deque()
        m, n = len(mat), len(mat[0])
        for r, c in product(range(m), range(n)):
            if mat[r][c] == 0:
                deq.append((r, c))
            else:
                mat[r][c] = -1
        directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
        while deq:
            r0, c0 = deq.popleft()
            for dr, dc in directions:
                r, c = r0 + dr, c0 + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] == -1:
                    mat[r][c] = mat[r0][c0] + 1
                    deq.append((r, c))
        return mat
