from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        result = 0
        length = 1
        counter = dict()
        s += "."
        for i in range(1, len(s)):
            prev, curr = s[i - 1], s[i]
            if prev == curr:
                length += 1
                continue
            result = max(result, length - 2)
            for j in range(length, result, -1):
                if j not in counter:
                    counter[j] = defaultdict(int)
                counter[j][prev] += length - j + 1
                if counter[j][prev] >= 3:
                    result = j
                    break
            length = 1
        return result if result > 0 else -1
