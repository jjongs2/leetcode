from collections import Counter


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for num in arr:
            if num == 0:
                if counter[0] > 1:
                    return True
            elif 2 * num in counter:
                return True
        return False
