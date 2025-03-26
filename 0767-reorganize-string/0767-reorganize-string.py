from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        result = [""]
        heap = [(-count, letter) for letter, count in Counter(s).items()]
        heapify(heap)

        def replace(count, letter):
            result.append(letter)
            if count < -1:
                heappush(heap, (count + 1, letter))

        while heap:
            count, letter = heappop(heap)
            if letter == result[-1]:
                if not heap:
                    return ""
                replace(*heappop(heap))
            replace(count, letter)
        return "".join(result)
