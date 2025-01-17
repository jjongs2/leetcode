class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        cumul = 0
        for x in derived:
            cumul ^= x
        return cumul == 0
