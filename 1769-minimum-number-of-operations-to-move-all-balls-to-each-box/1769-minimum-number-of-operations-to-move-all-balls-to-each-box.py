class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        left_ops = right_ops = 0
        left_balls = right_balls = 0
        for left in range(n):
            left_ops += left_balls
            result[left] += left_ops
            left_balls += int(boxes[left])
            right = n - left - 1
            right_ops += right_balls
            result[right] += right_ops
            right_balls += int(boxes[right])
        return result
