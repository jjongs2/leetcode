class Solution:
    VOWELS = set("aeiou")

    def countOfSubstrings(self, word: str, k: int) -> int:
        p_sums, p_indices = self._make_prefixes(word)
        vowels = dict()
        result = 0
        left = 0
        for right, letter in enumerate(word):
            if letter in self.VOWELS:
                vowels[letter] = vowels.get(letter, 0) + 1
            while len(vowels) == 5:
                p_sum = p_sums[left] + k
                if p_sum < len(p_indices):
                    result += max(0, p_indices[p_sum] - max(right, p_indices[p_sum - 1]))
                letter = word[left]
                if letter in self.VOWELS:
                    vowels[letter] -= 1
                    if vowels[letter] == 0:
                        del vowels[letter]
                left += 1
        return result

    def _make_prefixes(self, word):
        n = len(word)
        prefix_sums = [0] * (n + 1)
        prefix_indices = []
        for i, letter in enumerate(word):
            prefix_sums[i + 1] = prefix_sums[i]
            if letter not in self.VOWELS:
                prefix_sums[i + 1] += 1
                prefix_indices.append(i)
        prefix_indices.append(n)
        prefix_indices.append(0)
        return prefix_sums, prefix_indices
