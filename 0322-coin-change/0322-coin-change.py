from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counts = [inf for _ in range(amount + 1)]
        counts[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue
                counts[i] = min(counts[i], counts[i - coin] + 1)
        return counts[amount] if counts[amount] < inf else -1
