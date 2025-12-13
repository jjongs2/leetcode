CATEGORIES = {"electronics", "grocery", "pharmacy", "restaurant"}


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid_code(s):
            return s and all(c.isalnum() or c == '_' for c in s)

        return [a for _, a in sorted((b, a) for a, b, c in zip(code, businessLine, isActive) if is_valid_code(a) and b in CATEGORIES and c)]
