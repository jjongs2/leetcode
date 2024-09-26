from sortedcontainers import SortedList


class MyCalendar:
    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        event = (start, end)
        i = self.events.bisect_left(event)
        if i > 0 and self.events[i - 1][1] > start:
            return False
        if i < len(self.events) and end > self.events[i][0]:
            return False
        self.events.add(event)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
