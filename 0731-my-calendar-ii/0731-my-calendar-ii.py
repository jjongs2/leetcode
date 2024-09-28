from sortedcontainers import SortedList


class MyCalendarTwo:
    def __init__(self):
        self.single_bookings = SortedList()
        self.double_bookings = SortedList()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.double_bookings:
            if max(s, start) < min(e, end):
                return False
        for s, e in self.single_bookings:
            if max(s, start) < min(e, end):
                self.double_bookings.add((max(s, start), min(e, end)))
        self.single_bookings.add((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
