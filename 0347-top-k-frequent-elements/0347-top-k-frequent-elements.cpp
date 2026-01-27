class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;

        for (int num : nums) {
            freqs[num] += 1;
        }

        vector<int> result;
        vector<vector<int>> buckets(nums.size() + 1, vector<int>());

        for (auto [num, freq] : freqs) {
            buckets[freq].push_back(num);
        }
        for (auto rit = buckets.rbegin(); rit != buckets.rend(); ++rit) {
            if (rit->empty())
                continue;
            result.insert(result.end(), rit->begin(), rit->end());
            k -= rit->size();
            if (k == 0)
                break;
        }
        return result;
    }
};
