class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = dict.fromkeys("abc", 0)
        for char in s:
            total[char] += 1
        if any(total[c] < k for c in "abc"):
            return -1
        max_window = 0
        curr = dict.fromkeys("abc", 0)
        left = 0
        for right, char in enumerate(s):
            curr[char] += 1
            while left <= right and any(total[c] - curr[c] < k for c in "abc"):
                curr[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return len(s) - max_window
