#include <vector>

class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        if (n > 45)
            return {};
        vector<int> path;
        backtrack(k, n, 1, path);
        return result;
    }

private:
    void backtrack(int k, int n, int start, vector<int>& path) {
        if (k == 0) {
            if (n == 0)
                result.push_back(path);
            return;
        }
        for (int i = start; i <= 9 && i <= n; ++i) {
            path.push_back(i);
            backtrack(k - 1, n - i, i + 1, path);
            path.pop_back();
        }
    }

    vector<vector<int>> result;
};
