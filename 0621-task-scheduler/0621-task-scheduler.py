from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = tuple(Counter(tasks).values())
        max_count = max(counts)
        most_task_count = counts.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + most_task_count)
