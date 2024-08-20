class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sums = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = piles[i] + suffix_sums[i + 1]
        memo = dict()

        def take_stones(i, m):
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix_sums[i]
            if (i, m) in memo:
                return memo[(i, m)]
            max_count = suffix_sums[i] - min(
                take_stones(i + x, max(m, x)) for x in range(1, 2 * m + 1)
            )
            memo[(i, m)] = max_count
            return max_count

        return take_stones(0, 1)
