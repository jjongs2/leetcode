#include <queue>
#include <utility>
#include <vector>

const int DIRECTIONS[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size();
        int n = maze[0].size();
        int r = entrance[0];
        int c = entrance[1];
        queue<pair<int, int>> q{{make_pair(r, c)}};

        maze[r][c] = '+';
        for (int depth = 0; !q.empty(); ++depth) {
            for (int i = q.size(); i > 0; --i) {
                auto [r0, c0] = q.front();
                q.pop();
                for (auto [dr, dc] : DIRECTIONS) {
                    r = r0 + dr;
                    c = c0 + dc;
                    if (r < 0 || r >= m || c < 0 || c >= n) {
                        if (depth > 0)
                            return depth;
                        continue;
                    }
                    if (maze[r][c] == '+')
                        continue;
                    maze[r][c] = '+';
                    q.emplace(r, c);
                }
            }
        }
        return -1;
    }
};
