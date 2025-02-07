class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        int ball, old_color, new_color;
        int n = queries.size();
        vector<int> result(n);
        unordered_map<int, int> colors, freqs;

        for (int i = 0; i < n; ++i) {
            ball = queries[i][0];
            new_color = queries[i][1];
            if (colors.find(ball) != colors.end()) {
                old_color = colors[ball];
                freqs[old_color] -= 1;
                if (freqs[old_color] == 0)
                    freqs.erase(old_color);
            }
            colors[ball] = new_color;
            freqs[new_color] += 1;
            result[i] = freqs.size();
        }
        return result;
    }
};
