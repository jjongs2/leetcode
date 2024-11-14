class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def is_possible(x):
            count = 0
            for quantity in quantities:
                count += (quantity + x - 1) // x
                if count > n:
                    return False
            return True

        low, high = 0, max(quantities)
        while high - low > 1:
            mid = (low + high) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid
        return high
