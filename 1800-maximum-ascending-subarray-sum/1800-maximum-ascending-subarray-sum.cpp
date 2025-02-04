class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int max_sum = 0;
        int sum = nums[0];
        int size = nums.size();

        for (int i = 1; i < size; ++i) {
            if (nums[i - 1] < nums[i]) {
                sum += nums[i];
                continue;
            }
            max_sum = max(max_sum, sum);
            sum = nums[i];
        }
        return max(max_sum, sum);
    }
};
