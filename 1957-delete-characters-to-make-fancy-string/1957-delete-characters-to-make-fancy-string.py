class Solution:
    def makeFancyString(self, s: str) -> str:
        result = [""]
        count = 0
        for char in s:
            if char == result[-1]:
                if count == 2:
                    continue
                count += 1
            else:
                count = 1
            result.append(char)
        return "".join(result)
