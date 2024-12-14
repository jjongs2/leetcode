class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = 0
        start = 0
        min_val = max_val = nums[0]
        nums.append(-2)
        for end in range(1, len(nums)):
            num = nums[end]
            min_val = min(min_val, num)
            max_val = max(max_val, num)
            if max_val - min_val <= 2:
                continue
            size = end - start
            count += size * (size + 1) // 2
            min_val = max_val = num
            start = end - 1
            while abs(nums[start] - num) <= 2:
                min_val = min(min_val, nums[start])
                max_val = max(max_val, nums[start])
                start -= 1
            start += 1
            size = end - start
            count -= size * (size + 1) // 2
        return count
