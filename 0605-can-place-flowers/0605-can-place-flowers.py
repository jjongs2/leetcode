class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        available = 0
        length = len(flowerbed)
        flowerbed.append(0)
        for i in range(length):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                available += 1
                if available == n:
                    return True
                flowerbed[i] = 1
        return False
