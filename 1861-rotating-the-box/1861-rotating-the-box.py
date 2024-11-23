class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box[0])
        for row in box:
            right = n - 1
            for left in range(n - 1, -1, -1):
                if row[left] == "#":
                    row[left], row[right] = ".", "#"
                    right -= 1
                elif row[left] == "*":
                    right = left - 1
        return [list(reversed(col)) for col in zip(*box)]
