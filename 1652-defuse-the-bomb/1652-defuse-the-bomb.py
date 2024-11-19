class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if k == 0:
            return result
        sign = k < 0
        if sign:
            k = -k
            code = code[::-1]
        window_sum = sum(code[i] for i in range(k))
        for i in range(n):
            result[i - 1] = window_sum
            window_sum += code[(i + k) % n] - code[i]
        return result if not sign else result[::-1]
