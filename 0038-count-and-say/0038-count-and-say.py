class Solution:
    def countAndSay(self, n: int) -> str:
        prev = ["1"]
        for _ in range(n - 1):
            prev.append(".")
            curr = []
            i = 0
            for j in range(1, len(prev)):
                if prev[j] != prev[j - 1]:
                    curr.append(str(j - i))
                    curr.append(prev[i])
                    i = j
            prev = curr
        return "".join(prev)
