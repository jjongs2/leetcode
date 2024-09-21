class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(num):
            result.append(num)
            for digit in range(10):
                next_num = num * 10 + digit
                if next_num > n:
                    break
                dfs(next_num)

        for i in range(1, min(10, n + 1)):
            dfs(i)
        return result
