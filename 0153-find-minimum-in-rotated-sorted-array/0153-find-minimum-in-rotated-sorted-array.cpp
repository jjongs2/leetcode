class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        int low = 0;
        int high = n;

        while (high - low > 1) {
            int mid = (low + high) / 2;

            if (nums[low] < nums[mid]) {
                low = mid;
            } else {
                high = mid;
            }
        }
        return nums[high % n];
    }
};
