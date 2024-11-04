class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        count = 1
        word += "."
        prev = word[0]
        for i in range(1, len(word)):
            curr = word[i]
            if curr == prev and count < 9:
                count += 1
                continue
            result.append(f"{count}{prev}")
            count = 1
            prev = curr
        return "".join(result)
