class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        n = len(words)
        for i, word in enumerate(words):
            for j in range(n):
                if j == i:
                    continue
                if word in words[j]:
                    result.append(word)
                    break
        return result
