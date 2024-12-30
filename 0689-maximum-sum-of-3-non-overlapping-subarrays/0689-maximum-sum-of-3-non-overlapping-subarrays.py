class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1
        subsums = [0] * n
        for i in range(k):
            subsums[0] += nums[i]
        for curr in range(1, n):
            prev = curr - 1
            subsums[curr] = subsums[prev] - nums[prev] + nums[prev + k]
        maxsums = [(0, ()) for _ in range(4)]
        for i in range(n - 2 * k):
            for j in range(1, 4):
                maxsum, indices = maxsums[j - 1]
                if maxsums[j][0] - maxsum < subsums[i]:
                    maxsums[j] = (maxsum + subsums[i], indices + (i,))
                i += k
        return maxsums[-1][1]
