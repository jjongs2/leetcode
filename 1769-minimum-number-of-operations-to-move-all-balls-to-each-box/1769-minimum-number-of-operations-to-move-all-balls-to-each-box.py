class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        balls = [i for i, box in enumerate(boxes) if box == "1"]
        return [sum(abs(i - j) for j in balls) for i in range(n)]
