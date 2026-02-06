class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        int n = nums.size();
        int left = 0;
        int max_window = 0;

        for (int right = 0; right < n; ++right) {
            while (nums[left] < (nums[right] + k - 1) / k)
                ++left;
            max_window = max(max_window, right - left + 1);
        }
        return n - max_window;
    }
};
