class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        unordered_map<int, int> freqs;

        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                freqs[nums[i] * nums[j]] += 1;
        for (auto [_, freq] : freqs)
            if (freq >= 2)
                count += 4 * freq * (freq - 1);
        return count;
    }
};
