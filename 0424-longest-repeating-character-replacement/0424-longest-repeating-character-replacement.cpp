class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> freqs;
        int left = 0;
        int right = 0;
        int max_freq = 0;
        int n = s.size();

        while (right < n) {
            freqs[s[right]] += 1;
            max_freq = max(max_freq, freqs[s[right]]);
            right += 1;
            if (right - left - max_freq > k) {
                freqs[s[left]] -= 1;
                left += 1;
            }
        }
        return right - left;
    }
};
