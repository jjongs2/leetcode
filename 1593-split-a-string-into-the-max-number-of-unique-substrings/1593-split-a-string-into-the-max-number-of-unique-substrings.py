class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def backtrack(start, substrings):
            if start == n:
                return len(substrings)
            max_count = 0
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if substring not in substrings:
                    max_count = max(max_count, backtrack(end, substrings | {substring}))
            return max_count

        return backtrack(0, set())
