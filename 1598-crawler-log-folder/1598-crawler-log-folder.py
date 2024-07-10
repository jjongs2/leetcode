class Solution:
    def minOperations(self, logs: List[str]) -> int:
        degree = 0
        for log in logs:
            if log == "./":
                continue
            if log == "../":
                degree = max(degree - 1, 0)
            else:
                degree += 1
        return degree
