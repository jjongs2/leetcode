class Solution {
public:
    string reverseParentheses(string s) {
        string result;
        stack<int> opens;
        for (const char c : s) {
            if (c == '(') {
                opens.push(result.size());
            } else if (c == ')') {
                reverse(result.begin() + opens.top(), result.end());
                opens.pop();
            } else {
                result.push_back(c);
            }
        }
        return result;
    }
};
