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
            for i in range(len(stack)):
                top = stack.pop()
                if i % 2 == 0:
                    score += top
        return score
