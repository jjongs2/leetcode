class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        i = 0
        while i < n and colors[i] != colors[i - 1]:
            i += 1
        if i == n:
            return n
        count = 0
        first_size = i
        last_size = 0
        while True:
            start = i
            i += 1
            while i < n and colors[i] != colors[i - 1]:
                i += 1
            if i == n:
                last_size = n - start
                break
            size = i - start
            count += max(0, size - k + 1)
        count += max(0, first_size + last_size - k + 1)
        return count
