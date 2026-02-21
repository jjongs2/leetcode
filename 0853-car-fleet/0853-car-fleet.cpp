class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = speed.size();
        vector<int> index(n);

        for (int i = 0; i < n; ++i) {
            index[i] = i;
        }
        sort(index.begin(), index.end(),
             [&](int a, int b) { return position[a] > position[b]; });

        int count = 0;
        double prev_time = 0.0;

        for (int i : index) {
            double curr_time = static_cast<double>(target - position[i]) /
                               static_cast<double>(speed[i]);

            if (prev_time < curr_time) {
                count += 1;
                prev_time = curr_time;
            }
        }
        return count;
    }
};
