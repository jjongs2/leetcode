#include <algorithm>
#include <vector>

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        auto nth = nums.end() - k;
        nth_element(nums.begin(), nth, nums.end());
        return *nth;
    }
};
