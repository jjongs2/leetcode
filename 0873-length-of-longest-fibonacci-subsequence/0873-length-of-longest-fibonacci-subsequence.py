class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = {num: i for i, num in enumerate(arr)}
        n = len(arr)
        dp = [0] * n
        for i in range(n - 1):
            for j in range(i + 1, n):
                count = 3
                a, b = arr[i], arr[j]
                while (c := a + b) in nums:
                    dp[nums[c]] = max(dp[nums[c]], count)
                    count += 1
                    a, b = b, c
        return max(dp)
