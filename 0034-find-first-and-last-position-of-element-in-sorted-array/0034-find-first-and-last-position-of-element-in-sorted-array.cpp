class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.empty()) {
            return {-1, -1};
        }

        int low = 0;
        int high = nums.size();

        while (high - low > 1) {
            int mid = (low + high) / 2;
            if (nums[mid] <= target) {
                low = mid;
            } else {
                high = mid;
            }
        }

        if (nums[low] != target) {
            return {-1, -1};
        }

        int upper = low;
        low = -1;
        high = nums.size() - 1;

        while (high - low > 1) {
            int mid = (low + high) / 2;
            if (nums[mid] < target) {
                low = mid;
            } else {
                high = mid;
            }
        }
        return {high, upper};
    }
};
