class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int r = matrix.size();
        int c = matrix[0].size();

        int low = 0;
        int high = r * c;

        while (high - low > 1) {
            int mid = (low + high) / 2;
            if (matrix[mid / c][mid % c] <= target) {
                low = mid;
            } else {
                high = mid;
            }
        }
        return matrix[low / c][low % c] == target;
    }
};
