class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = m * n
        if size != len(original):
            return []
        return [original[i : i + n] for i in range(0, size, n)]
