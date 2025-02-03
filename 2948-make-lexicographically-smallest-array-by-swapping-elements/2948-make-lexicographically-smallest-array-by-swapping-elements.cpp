class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int size = nums.size();
        vector<int> result(size);
        vector<pair<int, int>> indexed_nums(size + 1);

        for (int i = 0; i < size; ++i)
            indexed_nums[i] = {nums[i], i};
        indexed_nums[size] = {numeric_limits<int>::max(), -1};
        sort(indexed_nums.begin(), indexed_nums.end());

        auto [prev, index] = indexed_nums.front();
        vector<int> indices{index};
        vector<int> values{prev};
        int sub_size;

        for (int i = 1; i <= size; ++i) {
            auto [curr, index] = indexed_nums[i];
            if (curr - prev > limit) {
                sort(indices.begin(), indices.end());
                sub_size = indices.size();
                for (int j = 0; j < sub_size; ++j)
                    result[indices[j]] = values[j];
                indices.clear();
                values.clear();
            }
            indices.push_back(index);
            values.push_back(curr);
            prev = curr;
        }
        return result;
    }
};
