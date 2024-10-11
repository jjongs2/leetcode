from heapq import heappop, heappush


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for friend, (arrival, leaving) in enumerate(times):
            events.append((leaving, 0, friend))
            events.append((arrival, 1, friend))
        events.sort()
        seats = dict()
        unoccupied = list(range(len(times)))
        for time, event_type, friend in events:
            if event_type == 0:
                heappush(unoccupied, seats.pop(friend))
            else:
                seats[friend] = heappop(unoccupied)
                if friend == targetFriend:
                    return seats[targetFriend]
