from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_counter, window_counter = Counter(t), Counter()
        count, required = 0, len(t_counter)
        start, end = 0, -1
        min_size = len(s)
        left = 0
        for right, char in enumerate(s):
            if char not in t_counter:
                continue
            window_counter[char] += 1
            if window_counter[char] == t_counter[char]:
                count += 1
            while count == required:
                while s[left] not in t_counter:
                    left += 1
                size = right - left
                if size < min_size:
                    min_size = size
                    start, end = left, right
                char = s[left]
                window_counter[char] -= 1
                if window_counter[char] < t_counter[char]:
                    count -= 1
                left += 1
        return s[start : end + 1]
