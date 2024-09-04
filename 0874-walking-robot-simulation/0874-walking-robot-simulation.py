DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        direction = 0
        max_distance = 0
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                dx, dy = DIRECTIONS[direction]
                for _ in range(command):
                    x, y = x + dx, y + dy
                    if (x, y) in obstacles:
                        x, y = x - dx, y - dy
                        break
                max_distance = max(max_distance, x * x + y * y)
        return max(max_distance, x * x + y * y)
