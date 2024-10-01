from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = Counter(num % k for num in arr)
        if counter[0] % 2 == 1:
            return False
        return all(counter[i] == counter[k - i] for i in range(1, (k + 1) // 2))
