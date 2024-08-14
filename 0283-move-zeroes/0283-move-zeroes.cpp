#include <algorithm>

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int nonzero_i = 0;
        int size = nums.size();
        for (int i = 0; i < size; ++i) {
            if (nums[i] == 0)
                continue;
            swap(nums[nonzero_i], nums[i]);
            nonzero_i += 1;
        }
    }
};
