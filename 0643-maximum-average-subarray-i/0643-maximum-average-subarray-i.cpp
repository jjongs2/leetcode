#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int curr_sum = reduce(nums.begin(), nums.begin() + k);
        int max_sum = curr_sum;
        int size = nums.size();
        for (int i = k; i < size; ++i) {
            curr_sum += nums[i] - nums[i - k];
            max_sum = max(max_sum, curr_sum);
        }
        return static_cast<double>(max_sum) / k;
    }
};
