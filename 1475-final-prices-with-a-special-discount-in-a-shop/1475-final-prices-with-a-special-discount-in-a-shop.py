class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for j, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                i = stack.pop()
                prices[i] -= price
            stack.append(j)
        return prices
