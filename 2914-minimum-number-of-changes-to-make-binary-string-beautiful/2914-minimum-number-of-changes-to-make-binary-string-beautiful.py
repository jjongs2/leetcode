class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        it = iter(s)
        while c1 := next(it, ""):
            c2 = next(it)
            if c1 != c2:
                count += 1
        return count
