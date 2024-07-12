class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int score = 0;
        int high = max(x, y);
        int low = min(x, y);
        char t0 = "ab"[x < y];
        char t1 = "ba"[x < y];
        vector<int> counts = {0, 0};
        deque<char> deq;
        for (char c : s) {
            if (c == t0) {
                deq.push_back(c);
                counts[0] += 1;
            } else if (c == t1) {
                if (!deq.empty() && deq.back() == t0) {
                    deq.pop_back();
                    counts[0] -= 1;
                    score += high;
                    continue;
                }
                deq.push_back(c);
                counts[1] += 1;
            } else if (!deq.empty()) {
                score += low * ranges::min(counts);
                deq.clear();
                counts = {0, 0};
            }
        }
        return score + low * ranges::min(counts);
    }
};
