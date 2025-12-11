from math import inf


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows, cols = dict(), dict()
        for r, c in buildings:
            min_c, max_c = rows[r] if r in rows else (inf, -inf)
            rows[r] = (min(c, min_c), max(c, max_c))
            min_r, max_r = cols[c] if c in cols else (inf, -inf)
            cols[c] = (min(r, min_r), max(r, max_r))
        result = 0
        for r, c in buildings:
            min_c, max_c = rows[r]
            min_r, max_r = cols[c]
            if min_c < c < max_c and min_r < r < max_r:
                result += 1
        return result
