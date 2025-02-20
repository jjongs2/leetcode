class Solution:
    def punishmentNumber(self, n: int) -> int:
        pnum = 0
        for num in range(1, n + 1):
            square = num * num
            if self._can_partition(num, str(square)):
                pnum += square
        return pnum

    def _can_partition(self, num, s, part_sum=0):
        if not s:
            return part_sum == num
        for i in range(1, len(s) + 1):
            part = int(s[:i])
            if part_sum + part > num:
                return False
            if self._can_partition(num, s[i:], part_sum + part):
                return True
        return False
