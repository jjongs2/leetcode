class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        curr_time = 0
        for arrival, time in customers:
            curr_time = max(curr_time, arrival) + time
            total_waiting_time += curr_time - arrival
        return total_waiting_time / len(customers)
