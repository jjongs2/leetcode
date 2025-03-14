class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def is_possible(pile_size):
            pile_count = 0
            for candy in candies:
                pile_count += candy // pile_size
                if pile_count >= k:
                    return True
            return False

        low, high = 0, max(candies) + 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_possible(mid):
                low = mid
            else:
                high = mid
        return low
