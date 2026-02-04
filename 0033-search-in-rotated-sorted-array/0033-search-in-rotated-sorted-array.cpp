class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size();

        nums.push_back(nums.front());
        while (high - low > 1) {
            int mid = (low + high) / 2;
            if (nums[low] < nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid;
                } else {
                    low = mid;
                }
            } else {
                if (nums[mid] <= target && target < nums[high]) {
                    low = mid;
                } else {
                    high = mid;
                }
            }
        }
        return nums[low] == target ? low : -1;
    }
};
