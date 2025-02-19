class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 3 * 2 ** (n - 1)
        if k > count:
            return ""
        sets = {"a": "bc", "b": "ac", "c": "ab"}
        count //= 3
        i, k = divmod(k - 1, count)
        result = ["abc"[i]]
        while count > 1:
            count //= 2
            i, k = divmod(k, count)
            result.append(sets[result[-1]][i])
        return "".join(result)
