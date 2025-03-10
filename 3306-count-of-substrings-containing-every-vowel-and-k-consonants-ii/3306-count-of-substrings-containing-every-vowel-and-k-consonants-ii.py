class Solution:
    VOWELS = set("aeiou")

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._helper(word, k) - self._helper(word, k + 1)

    def _helper(self, word, k):
        n = len(word)
        vowels = dict()
        consonants = 0
        result = 0
        left = 0
        for right, letter in enumerate(word):
            if letter in self.VOWELS:
                vowels[letter] = vowels.get(letter, 0) + 1
            else:
                consonants += 1
            while len(vowels) == 5 and consonants >= k:
                result += n - right
                letter = word[left]
                if letter in self.VOWELS:
                    vowels[letter] -= 1
                    if vowels[letter] == 0:
                        del vowels[letter]
                else:
                    consonants -= 1
                left += 1
        return result
