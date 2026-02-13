class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 0;
        int high = *max_element(piles.begin(), piles.end());

        auto is_possible = [&](int k) -> bool {
            int64_t hour = 0;

            for (int pile : piles) {
                hour += (pile + k - 1) / k;
            }
            return hour <= h;
        };

        while (high - low > 1) {
            int mid = low + (high - low) / 2;

            if (is_possible(mid)) {
                high = mid;
            } else {
                low = mid;
            }
        }
        return high;
    }
};
