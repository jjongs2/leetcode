class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int s_size = s.size();
        int p_size = p.size();

        if (s_size < p_size) {
            return {};
        }

        vector<int> result;
        vector<int> target(26, 0);
        vector<int> window(26, 0);

        for (int i = 0; i < p_size; ++i) {
            target[p[i] - 'a'] += 1;
            window[s[i] - 'a'] += 1;
        }
        if (window == target) {
            result.push_back(0);
        }

        for (int i = p_size; i < s_size; ++i) {
            window[s[i] - 'a'] += 1;
            window[s[i - p_size] - 'a'] -= 1;
            if (window == target) {
                result.push_back(i - p_size + 1);
            }
        }
        return result;
    }
};
