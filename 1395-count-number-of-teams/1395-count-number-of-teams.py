class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)
        for j in range(1, n - 1):
            rating_j = rating[j]
            left = sum(rating[i] < rating_j for i in range(j))
            right = sum(rating_j < rating[k] for k in range(j + 1, n))
            count += left * right + (j - left) * (n - (j + 1) - right)
        return count
