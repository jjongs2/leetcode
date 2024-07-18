class Solution:
    def myAtoi(self, s: str) -> int:
        string = s.strip()
        if not string:
            return 0
        int_min, int_max = -(2**31), 2**31 - 1
        sign = -1 if string[0] == "-" else 1
        start = 1 if string[0] in ("-", "+") else 0
        result = 0
        for char in string[start:]:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
            if sign * result < int_min:
                return int_min
            if sign * result > int_max:
                return int_max
        return sign * result
