class Solution:
    VOWELS = set("aeiou")

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sums = [0] * (len(words) + 1)
        for i, word in enumerate(words, start=1):
            prefix_sums[i] = prefix_sums[i - 1]
            if word[0] in self.VOWELS and word[-1] in self.VOWELS:
                prefix_sums[i] += 1
        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            ans[i] = prefix_sums[r + 1] - prefix_sums[l]
        return ans
