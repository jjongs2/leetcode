from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = []
        counter = Counter(s)
        sorted_items = sorted(counter.items())
        while sorted_items:
            c1, n1 = sorted_items[-1]
            result.append(c1 * min(n1, repeatLimit))
            if n1 <= repeatLimit:
                sorted_items.pop()
                continue
            if len(sorted_items) == 1:
                break
            sorted_items[-1] = (c1, n1 - repeatLimit)
            c2, n2 = sorted_items[-2]
            result.append(c2)
            if n2 == 1:
                sorted_items.pop(-2)
            else:
                sorted_items[-2] = (c2, n2 - 1)
        return "".join(result)
