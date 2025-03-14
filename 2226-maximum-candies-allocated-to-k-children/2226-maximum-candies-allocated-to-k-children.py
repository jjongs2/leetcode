class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def is_possible(pile_size):
            return sum(candy // pile_size for candy in candies) >= k

        low, high = 0, max(candies) + 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_possible(mid):
                low = mid
            else:
                high = mid
        return low
