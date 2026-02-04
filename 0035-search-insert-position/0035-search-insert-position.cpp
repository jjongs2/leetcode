class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (target <= nums.front()) {
            return 0;
        }

        int low = 0;
        int high = nums.size();

        while (high - low > 1) {
            int mid = (low + high) / 2;
            if (nums[mid] < target) {
                low = mid;
            } else {
                high = mid;
            }
        }
        return high;
    }
};
