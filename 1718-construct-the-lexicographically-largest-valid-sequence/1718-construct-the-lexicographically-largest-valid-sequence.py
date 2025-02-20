class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2 * n - 1
        seq = [0] * length
        used = [False] * (n + 1)

        def backtrack(i):
            while i < length and seq[i] != 0:
                i += 1
            if i == length:
                return True
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if seq[i] != 0:
                    continue
                if num > 1:
                    if i + num < length and seq[i + num] == 0:
                        seq[i + num] = num
                    else:
                        continue
                seq[i] = num
                used[num] = True
                if backtrack(i + 1):
                    return True
                used[num] = False
                seq[i] = 0
                if num > 1:
                    seq[i + num] = 0
            return False

        backtrack(0)
        return seq
