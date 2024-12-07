class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def is_possible(size):
            count = 0
            for num in nums:
                count += (num - 1) // size
                if count > maxOperations:
                    return False
            return True

        low, high = 1, max(nums)
        while high - low > 1:
            mid = (low + high) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid
        return high
