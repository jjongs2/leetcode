class Solution {
public:
    static constexpr pair<int, int> DIRECTIONS[4] = {
        {0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    int findMaxFish(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int max_sum = 0;
        stack<pair<int, int>> s;

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 0)
                    continue;
                int sum = grid[r][c];
                grid[r][c] = 0;
                s.emplace(r, c);
                while (!s.empty()) {
                    auto [r1, c1] = s.top();
                    s.pop();
                    for (auto [dr, dc] : DIRECTIONS) {
                        int r2 = r1 + dr;
                        int c2 = c1 + dc;
                        if (r2 < 0 || r2 >= m || c2 < 0 || c2 >= n)
                            continue;
                        if (grid[r2][c2] == 0)
                            continue;
                        sum += grid[r2][c2];
                        grid[r2][c2] = 0;
                        s.emplace(r2, c2);
                    }
                }
                max_sum = max(max_sum, sum);
            }
        }
        return max_sum;
    }
};
