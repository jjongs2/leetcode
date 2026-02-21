class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        static unordered_map<string, function<int(int, int)>> op{{
            {"+", plus<int>()},
            {"-", minus<int>()},
            {"*", multiplies<int>()},
            {"/", divides<int>()},
        }};

        stack<int> stk;

        for (const auto& token : tokens) {
            if (isdigit(token.back())) {
                stk.push(stoi(token));
            } else {
                int rhs = stk.top();
                stk.pop();
                int lhs = stk.top();
                stk.pop();
                stk.push(op[token](lhs, rhs));
            }
        }
        return stk.top();
    }
};
