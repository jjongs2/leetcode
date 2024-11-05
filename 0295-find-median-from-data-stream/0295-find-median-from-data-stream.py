from sortedcontainers import SortedList


class MedianFinder:
    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)

    def findMedian(self) -> float:
        half, is_odd = divmod(len(self.arr), 2)
        if is_odd:
            return self.arr[half]
        return (self.arr[half - 1] + self.arr[half]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
