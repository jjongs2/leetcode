class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(detail[-4:-2]) > 60 for detail in details)
