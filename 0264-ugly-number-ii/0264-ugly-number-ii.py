class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        indices = {2: 0, 3: 0, 5: 0}
        for _ in range(n - 1):
            num = min(nums[v] * k for k, v in indices.items())
            nums.append(num)
            for k, v in indices.items():
                if num == nums[v] * k:
                    indices[k] += 1
        return nums[-1]
