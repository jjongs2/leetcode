from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return self._backtrack(Counter(tiles))

    def _backtrack(self, freqs):
        count = 0
        for letter, freq in freqs.items():
            if freq == 0:
                continue
            freqs[letter] -= 1
            count += 1 + self._backtrack(freqs)
            freqs[letter] += 1
        return count
