class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        longer, shorter = sentence1.split(), sentence2.split()
        if len(longer) < len(shorter):
            longer, shorter = shorter, longer
        n = len(shorter)
        left, right = 0, -1
        while left < n and shorter[left] == longer[left]:
            left += 1
        while right >= left - n and shorter[right] == longer[right]:
            right -= 1
        return left - n == right + 1
