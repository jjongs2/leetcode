class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        int n = nums.size();
        int left, right, sum;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n; ++i) {
            if (nums[i] > 0)
                break;
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            left = i + 1;
            right = n - 1;
            while (left < right) {
                sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    left += 1;
                    right -= 1;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left += 1;
                    }
                    while (left < right && nums[right] == nums[right + 1]) {
                        right -= 1;
                    }
                } else if (sum < 0) {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        return result;
    }
};
