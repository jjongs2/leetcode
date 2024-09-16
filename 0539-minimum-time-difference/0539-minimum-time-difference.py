DAY_IN_MINUTES = 1440


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > DAY_IN_MINUTES:
            return 0

        def to_minutes(time):
            h, m = map(int, time.split(":"))
            return 60 * h + m

        minutes = sorted(map(to_minutes, timePoints))
        minutes.append(minutes[0] + DAY_IN_MINUTES)
        min_diff = DAY_IN_MINUTES
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        return min_diff
