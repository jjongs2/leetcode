class Solution:
    def countLargestGroup(self, n: int) -> int:
        sizes = [0] * 37
        for x in range(1, n + 1):
            sizes[sum(map(int, str(x)))] += 1
        max_size, max_count = 0, 0
        for size in sizes:
            if size > max_size:
                max_size = size
                max_count = 1
            elif size == max_size:
                max_count += 1
        return max_count
