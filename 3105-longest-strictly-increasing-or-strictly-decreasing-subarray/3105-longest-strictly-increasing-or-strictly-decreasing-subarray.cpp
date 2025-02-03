class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int n = nums.size();
        int inc_count = 1;
        int dec_count = 1;
        int result = 1;

        for (int i = 1; i < n; ++i) {
            if (nums[i - 1] < nums[i]) {
                inc_count += 1;
                dec_count = 1;
            } else if (nums[i - 1] > nums[i]) {
                inc_count = 1;
                dec_count += 1;
            } else {
                inc_count = 1;
                dec_count = 1;
            }
            result = max({result, inc_count, dec_count});
        }
        return result;
    }
};
