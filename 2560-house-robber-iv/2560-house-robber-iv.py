class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_possible(cap):
            count = 0
            prev = False
            for num in nums:
                if prev:
                    prev = False
                elif num <= cap:
                    count += 1
                    prev = True
            return count >= k

        low, high = 0, max(nums)
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid
        return high
