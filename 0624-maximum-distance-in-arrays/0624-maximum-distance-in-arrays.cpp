#include <algorithm>
#include <vector>

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int max_d = 0;
        int total_min = arrays[0].front();
        int total_max = arrays[0].back();
        int m = arrays.size();
        for (int i = 1; i < m; ++i) {
            int curr_min = arrays[i].front();
            int curr_max = arrays[i].back();
            max_d = max({max_d, curr_max - total_min, total_max - curr_min});
            total_max = max(total_max, curr_max);
            total_min = min(total_min, curr_min);
        }
        return max_d;
    }
};
