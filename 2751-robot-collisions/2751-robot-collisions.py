class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        remains = []
        stack = []
        indices = sorted(range(len(positions)), key=lambda i: positions[i])
        for i in indices:
            if directions[i] == "R":
                stack.append(i)
                continue
            while stack and healths[i] > healths[stack[-1]]:
                healths[i] -= 1
                stack.pop()
            if not stack:
                remains.append((i, healths[i]))
            elif healths[i] < healths[stack[-1]]:
                healths[stack[-1]] -= 1
            else:
                stack.pop()
        remains.extend((i, healths[i]) for i in stack)
        return [health for _, health in sorted(remains)]
