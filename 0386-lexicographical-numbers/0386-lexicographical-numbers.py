class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = [1]
        k = 1
        for _ in range(n - 1):
            k *= 10
            if k > n:
                while k % 10 == 9 or k >= n:
                    k //= 10
                k += 1
            result.append(k)
        return result
