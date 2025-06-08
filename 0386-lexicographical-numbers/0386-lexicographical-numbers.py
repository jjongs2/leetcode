class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def helper(num):
            for k in range(num, num + 10):
                if k <= n:
                    result.append(k)
                    helper(10 * k)

        for k in range(1, 10):
            if k <= n:
                result.append(k)
                helper(10 * k)
        return result
