from math import inf


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        childrens = [[] for _ in range(n + 1)]
        for parent, child in hierarchy:
            childrens[parent].append(child)

        def merge(dp1, dp2):
            new_dp = [-inf] * (budget + 1)
            for c1 in range(budget + 1):
                if dp1[c1] == -inf:
                    continue
                for c2 in range(budget + 1 - c1):
                    if dp2[c2] == -inf:
                        continue
                    new_dp[c1 + c2] = max(new_dp[c1 + c2], dp1[c1] + dp2[c2])
            return new_dp

        def dfs(v):
            dp = [[-inf] * (budget + 1) for _ in range(2)]
            dp[0][0] = dp[1][0] = 0
            for child in childrens[v]:
                child_dp = dfs(child)
                dp[0] = merge(dp[0], child_dp[0])
                dp[1] = merge(dp[1], child_dp[1])
            result = [[-inf] * (budget + 1) for _ in range(2)]
            v -= 1
            price, half_price = present[v], present[v] // 2
            for b in range(budget + 1):
                if dp[0][b] != -inf:
                    result[0][b] = max(result[0][b], dp[0][b])
                    result[1][b] = max(result[1][b], dp[0][b])
                b0 = b - price
                if b0 >= 0 and dp[1][b0] != -inf:
                    result[0][b] = max(result[0][b], dp[1][b0] + future[v] - price)
                b1 = b - half_price
                if b1 >= 0 and dp[1][b1] != -inf:
                    result[1][b] = max(result[1][b], dp[1][b1] + future[v] - half_price)
            return result

        profits, _ = dfs(1)
        return max(0, max(profits))
