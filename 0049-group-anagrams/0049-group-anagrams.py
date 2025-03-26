class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        a = ord("a")
        for s in strs:
            freqs = [0] * 26
            for c in map(ord, s):
                freqs[c - a] += 1
            groups.setdefault(tuple(freqs), []).append(s)
        return list(groups.values())
