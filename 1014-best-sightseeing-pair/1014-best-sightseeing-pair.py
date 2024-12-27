class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_prev = values[0]
        for i in range(1, len(values)):
            max_prev -= 1
            max_score = max(max_score, max_prev + values[i])
            max_prev = max(max_prev, values[i])
        return max_score
