from math import inf


class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums.append(inf)
        score = 0
        stack = []
        for num in nums:
            if not stack or stack[-1] > num:
                stack.append(num)
                continue
            for i, n in enumerate(reversed(stack)):
                if i % 2 == 0:
                    score += n
            stack = []
        return score
