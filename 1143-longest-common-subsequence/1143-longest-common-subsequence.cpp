#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        if (text1.size() < text2.size())
            text1.swap(text2);
        int size1 = text1.size();
        int size2 = text2.size();
        vector<int> dp(size2 + 1);
        for (char c1: text1) {
            int prev = 0;
            for (int i = 1; i <= size2; ++i) {
                int temp = dp[i];
                char c2 = text2[i - 1];
                if (c1 == c2)
                    dp[i] = prev + 1;
                else
                    dp[i] = max(dp[i], dp[i - 1]);
                prev = temp;
            }
        }
        return dp.back();
    }
};
