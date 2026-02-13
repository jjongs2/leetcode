class Solution {
public:
    inline static const unordered_map<char, char> CLOSE_TO_OPEN{
        {')', '('}, {'}', '{'}, {']', '['}
    };

    bool isValid(string s) {
        if (s.size() % 2 == 1) {
            return false;
        }

        stack<char> stk;

        for (char c : s) {
            if (CLOSE_TO_OPEN.find(c) == CLOSE_TO_OPEN.end()) {
                stk.push(c);
            } else if (!stk.empty() && stk.top() == CLOSE_TO_OPEN.at(c)) {
                stk.pop();
            } else {
                return false;
            }
        }
        return stk.empty();
    }
};
