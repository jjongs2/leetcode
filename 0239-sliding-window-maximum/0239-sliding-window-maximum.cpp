class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> deq;
        int n = nums.size();

        auto slide = [&](int index) {
            while (!deq.empty() && nums[index] >= nums[deq.back()]) {
                deq.pop_back();
            }
            deq.push_back(index);
        };

        for (int i = 0; i < k; ++i) {
            slide(i);
        }
        result.push_back(nums[deq.front()]);

        for (int i = k; i < n; ++i) {
            if (i - deq.front() == k) {
                deq.pop_front();
            }
            slide(i);
            result.push_back(nums[deq.front()]);
        }
        return result;
    }
};
