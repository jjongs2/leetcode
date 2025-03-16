from math import isqrt


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_possible(time):
            return sum(isqrt(time // rank) for rank in ranks) >= cars

        low = 0
        high = min(ranks) * cars * cars
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid
        return high
