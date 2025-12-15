class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0
        days = 1
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                days += 1
            else:
                result += days * (days + 1) // 2
                days = 1
        result += days * (days + 1) // 2
        return result
