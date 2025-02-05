class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int n = s1.size();
        int i = -1;
        int diff_count = 0;

        for (int j = 0; j < n; ++j) {
            if (s1[j] == s2[j])
                continue;
            if (diff_count == 2)
                return false;
            if (i == -1)
                i = j;
            else if (s1[i] != s2[j] || s2[i] != s1[j])
                return false;
            diff_count += 1;
        }
        return diff_count % 2 == 0;
    }
};
