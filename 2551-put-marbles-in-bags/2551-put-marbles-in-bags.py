class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        adj_sums = sorted(weights[i] + weights[i + 1] for i in range(n - 1))
        return sum(adj_sums[n - 2 - i] - adj_sums[i] for i in range(min(k - 1, n - k)))
