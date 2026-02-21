class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int half = (m + n + 1) / 2;
        int low = 0;
        int high = m;

        while (true) {
            int i = (low + high) / 2;
            int j = half - i;

            int left1 = (i > 0) ? nums1[i - 1] : INT_MIN;
            int right1 = (i < m) ? nums1[i] : INT_MAX;
            int left2 = (j > 0) ? nums2[j - 1] : INT_MIN;
            int right2 = (j < n) ? nums2[j] : INT_MAX;

            if (left1 > right2) {
                high = i;
            } else if (left2 > right1) {
                low = i + 1;
            } else {
                double left = static_cast<double>(max(left1, left2));
                double right = static_cast<double>(min(right1, right2));
                return ((m + n) % 2 == 1) ? left : (left + right) / 2.0;
            }
        }
    };
};
