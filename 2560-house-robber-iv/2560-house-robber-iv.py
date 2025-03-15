class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_possible(cap):
            o, x = 0, 0
            for num in nums:
                if num <= cap:
                    o, x = x + 1, max(o, x)
                else:
                    x = max(o, x)
            return max(o, x) >= k

        low, high = 0, max(nums)
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid
        return high
