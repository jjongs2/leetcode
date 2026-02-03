class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        auto prev = nums.begin();
        auto curr = prev + 1;
        while (curr != nums.end() && *prev < *curr) {
            ++prev;
            ++curr;
        }
        auto p = prev;
        if (p == nums.begin()) {
            return false;
        }
        while (curr != nums.end() && *prev > *curr) {
            ++prev;
            ++curr;
        }
        auto q = prev;
        if (q == p || curr == nums.end()) {
            return false;
        }
        while (curr != nums.end() && *prev < *curr) {
            ++prev;
            ++curr;
        }
        return curr == nums.end();
    }
};
