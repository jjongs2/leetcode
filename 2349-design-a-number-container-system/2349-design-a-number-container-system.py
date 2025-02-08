from collections import defaultdict
from sortedcontainers import SortedList


class NumberContainers:
    def __init__(self):
        self.containers = dict()
        self.indices = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.containers:
            self.indices[self.containers[index]].remove(index)
        self.containers[index] = number
        self.indices[number].add(index)

    def find(self, number: int) -> int:
        return self.indices[number][0] if self.indices[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
