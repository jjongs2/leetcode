class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        end = len(candidates)
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return
            prev = 0
            for i in range(start, end):
                num = candidates[i]
                if num == prev:
                    continue
                if num > target:
                    return
                path.append(num)
                backtrack(i + 1, target - num, path)
                path.pop()
                prev = num

        backtrack(0, target, [])
        return result
