class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = window_sum = 0
        counter = dict()
        for i, right in enumerate(nums):
            window_sum += right
            counter[right] = counter.get(right, 0) + 1
            if i >= k:
                left = nums[i - k]
                window_sum -= left
                counter[left] -= 1
                if counter[left] == 0:
                    del counter[left]
            if len(counter) == k:
                max_sum = max(max_sum, window_sum)
        return max_sum
