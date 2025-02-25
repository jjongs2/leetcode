class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + arr[i]
        odd_count = sum(prefix_sum % 2 == 1 for prefix_sum in prefix_sums)
        return (odd_count * (n + 1 - odd_count)) % (10**9 + 7)
