class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_step(start):
            total_step = 0
            step = 1
            while start <= n:
                total_step += min(step, n - start + 1)
                step *= 10
                start *= 10
            return total_step

        num = 1
        k -= 1
        while k > 0:
            step = count_step(num)
            if k < step:
                num *= 10
                k -= 1
            else:
                num += 1
                k -= step
        return num
