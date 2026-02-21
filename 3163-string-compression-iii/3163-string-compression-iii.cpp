class Solution {
public:
    string compressedString(string word) {
        word.push_back('.');

        string result;
        char prev = word[0];
        int count = 1;
        int n = word.size();

        for (int i = 1; i < n; ++i) {
            char curr = word[i];

            if (curr == prev && count < 9) {
                count += 1;
            } else {
                result.push_back('0' + count);
                result.push_back(prev);
                prev = curr;
                count = 1;
            }
        }
        return result;
    }
};
