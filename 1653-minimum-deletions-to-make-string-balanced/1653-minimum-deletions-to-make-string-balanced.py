class Solution:
    def minimumDeletions(self, s: str) -> int:
        delete_count, b_count = 0, 0
        for char in s:
            if char == "b":
                b_count += 1
            elif b_count > 0:
                b_count -= 1
                delete_count += 1
        return delete_count
