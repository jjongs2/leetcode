from collections import defaultdict


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_diff, y_diff = defaultdict(int), defaultdict(int)
        for x1, y1, x2, y2 in rectangles:
            x_diff[x1 + 1] += 1
            x_diff[x2] -= 1
            y_diff[y1 + 1] += 1
            y_diff[y2] -= 1
        return self._is_possible(x_diff) or self._is_possible(y_diff)

    @staticmethod
    def _is_possible(diff):
        section = 0
        rectangle = 0
        for pos in sorted(diff):
            rectangle += diff[pos]
            if rectangle == 0:
                section += 1
                if section == 3:
                    return True
        return False
