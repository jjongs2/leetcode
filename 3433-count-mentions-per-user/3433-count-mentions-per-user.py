from collections import deque


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        for event in events:
            event[1] = int(event[1])
        events.sort(key=lambda x: (x[1], x[0] == "MESSAGE"))
        mentions = [0] * numberOfUsers
        all_count = 0
        online = set(range(numberOfUsers))
        offline = deque()
        for event_type, timestamp, target in events:
            while offline and timestamp >= offline[0][0]:
                _, i = offline.popleft()
                online.add(i)
            if event_type == "OFFLINE":
                tgt = int(target)
                online.remove(tgt)
                offline.append((timestamp + 60, tgt))
            elif target == "ALL":
                all_count += 1
            elif target == "HERE":
                for i in online:
                    mentions[i] += 1
            else:
                for tgt in target.split():
                    mentions[int(tgt[2:])] += 1
        for i in range(numberOfUsers):
            mentions[i] += all_count
        return mentions
