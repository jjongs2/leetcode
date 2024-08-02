from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        p_counter = Counter(p)
        word_counter = Counter(s[:p_len])
        result = [0] if word_counter == p_counter else []
        for i in range(s_len - p_len):
            word_counter[s[i]] -= 1
            word_counter[s[i + p_len]] += 1
            if word_counter == p_counter:
                result.append(i + 1)
        return result
