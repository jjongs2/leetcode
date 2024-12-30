class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1
        subsums = [0] * n
        for i in range(k):
            subsums[0] += nums[i]
        for curr in range(1, n):
            prev = curr - 1
            subsums[curr] = subsums[prev] - nums[prev] + nums[prev + k]
        dp = [[(0, []) for _ in range(4)] for _ in range(n)]
        for i in range(k):
            curr = dp[i][1] = dp[i - 1][1]
            if curr[0] < subsums[i]:
                dp[i][1] = (subsums[i], [i])
        for i in range(k, n):
            for j in range(1, 4):
                curr = dp[i][j] = dp[i - 1][j]
                prev = dp[i - k][j - 1]
                if curr[0] < prev[0] + subsums[i]:
                    dp[i][j] = (prev[0] + subsums[i], prev[1] + [i])
        return dp[-1][-1][1]
