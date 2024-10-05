from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False
        s1_counter = Counter(s1)
        s2_counter = Counter()
        for i in range(s1_len):
            s2_counter[s2[i]] += 1
        for i in range(s2_len - s1_len):
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[i]] -= 1
            s2_counter[s2[i + s1_len]] += 1
        return s1_counter == s2_counter
