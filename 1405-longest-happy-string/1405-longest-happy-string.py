from heapq import heappop, heappush


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, letter in ((a, "a"), (b, "b"), (c, "c")):
            if count > 0:
                heappush(heap, (-count, letter))
        result = [""]
        same = 0
        while heap:
            count, letter = heappop(heap)
            if result[-1] != letter:
                same = 1
            else:
                same += 1
                if same == 3:
                    if not heap:
                        break
                    next_count, next_letter = heappop(heap)
                    result.append(next_letter)
                    same = 1
                    if next_count < -1:
                        heappush(heap, (next_count + 1, next_letter))
            result.append(letter)
            if count < -1:
                heappush(heap, (count + 1, letter))
        return "".join(result)
