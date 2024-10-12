from collections import defaultdict


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        counts = defaultdict(int)
        for left, right in intervals:
            counts[left] += 1
            counts[right + 1] -= 1
        result = 0
        count_sum = 0
        for _, count in sorted(counts.items()):
            count_sum += count
            result = max(result, count_sum)
        return result
