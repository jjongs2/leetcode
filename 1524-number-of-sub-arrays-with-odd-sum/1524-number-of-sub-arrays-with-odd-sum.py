class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = 0
        prefix_sum = 0
        counts = [1, 0]
        for num in arr:
            prefix_sum += num
            is_odd = prefix_sum % 2
            result += counts[is_odd ^ 1]
            counts[is_odd] += 1
        return result % (10**9 + 7)
