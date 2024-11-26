from collections import deque


class Solution:
    ANSWER = "123450"
    DIRECTIONS = {
        0: (1, 3),
        1: (0, 2, 4),
        2: (1, 5),
        3: (0, 4),
        4: (1, 3, 5),
        5: (2, 4),
    }

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        state = "".join(str(num) for row in board for num in row)
        if state == self.ANSWER:
            return 0
        q = deque([(state, state.find("0"))])
        visited = {state}
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                s0, i0 = q.popleft()
                for i in self.DIRECTIONS[i0]:
                    s = list(s0)
                    s[i0], s[i] = s[i], s[i0]
                    s = "".join(s)
                    if s in visited:
                        continue
                    if s == self.ANSWER:
                        return depth
                    visited.add(s)
                    q.append((s, i))
        return -1
