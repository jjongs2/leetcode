class Solution {
public:
    int trap(vector<int>& height) {
        int result = 0;
        int left = 0;
        int right = height.size() - 1;
        int max_left_h = 0;
        int max_right_h = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                max_left_h = max(max_left_h, height[left]);
                result += max_left_h - height[left];
                left += 1;
            } else {
                max_right_h = max(max_right_h, height[right]);
                result += max_right_h - height[right];
                right -= 1;
            }
        }
        return result;
    }
};
