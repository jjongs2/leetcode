class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_list = list(s)
        for i in spaces:
            s_list[i] = " " + s_list[i]
        return "".join(s_list)
