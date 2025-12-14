MOD = 10**9 + 7


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        result = 1
        seat_count = 0
        start = -1
        for i, c in enumerate(corridor):
            if c == "S":
                seat_count += 1
                if seat_count > 2 and seat_count % 2 == 1:
                    result = (result * (i - start)) % MOD
                start = i
        return result if seat_count > 0 and seat_count % 2 == 0 else 0
