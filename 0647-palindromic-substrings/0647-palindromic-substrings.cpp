class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        int m = 2 * n + 1;
        string t(m, '#');

        for (int i = 0; i < n; ++i) {
            t[2 * i + 1] = s[i];
        }

        vector<int> p(m, 0);
        int c = 0;
        int r = 0;
        int left, right;

        for (int i = 0; i < m; ++i) {
            if (i < r) {
                p[i] = min(r - i, p[2 * c - i]);
            }

            left = i - p[i] - 1;
            right = i + p[i] + 1;
            while (left >= 0 && right < m && t[left] == t[right]) {
                p[i] += 1;
                left -= 1;
                right += 1;
            }

            if (i + p[i] > r) {
                r = i + p[i];
                c = i;
            }
        }

        int count = n;

        for (int i = 0; i < m; ++i) {
            count += p[i] / 2;
        }
        return count;
    }
};
