class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(num for num in banned if num <= n)
        count = curr_sum = 0
        for num in range(1, n + 1):
            if num in banned:
                continue
            curr_sum += num
            if curr_sum > maxSum:
                break
            count += 1
        return count
