class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        temp = []
        pattern += "I"
        for num, char in enumerate(pattern, start=1):
            temp.append(num)
            if char == "I":
                result.extend(reversed(temp))
                temp = []
        return "".join(map(str, result))
