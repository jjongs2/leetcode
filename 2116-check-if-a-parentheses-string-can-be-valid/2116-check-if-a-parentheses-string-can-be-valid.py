class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        if not self._is_possible(s, locked, "("):
            return False
        return self._is_possible(reversed(s), reversed(locked), ")")

    @staticmethod
    def _is_possible(string, lock_info, open_bracket):
        locked_depth = 0
        unlocked_count = 0
        for char, lock in zip(string, lock_info):
            if lock == "0":
                unlocked_count += 1
            elif char == open_bracket:
                locked_depth += 1
            elif locked_depth > 0:
                locked_depth -= 1
            elif unlocked_count > 0:
                unlocked_count -= 1
            else:
                return False
        return locked_depth <= unlocked_count
