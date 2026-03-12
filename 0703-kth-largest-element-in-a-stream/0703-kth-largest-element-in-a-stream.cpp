class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k_(k) {
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        if (heap_.size() < k_) {
            heap_.push(val);
        } else if (val > heap_.top()) {
            heap_.push(val);
            heap_.pop();
        }
        return heap_.top();
    }

private:
    int k_;
    priority_queue<int, vector<int>, greater<int>> heap_;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
