class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0")
            return "0";

        int n1 = num1.size();
        int n2 = num2.size();
        vector<int> result(n1 + n2, 0);

        for (int i = n1 - 1; i >= 0; --i) {
            for (int j = n2 - 1; j >= 0; --j) {
                int k = i + j + 1;
                result[k] += (num1[i] - '0') * (num2[j] - '0');
                result[k - 1] += result[k] / 10;
                result[k] %= 10;
            }
        }

        string answer;
        answer.reserve(n1 + n2);
        for (int digit : result) {
            if (!(answer.empty() && digit == 0)) {
                answer.push_back('0' + digit);
            }
        }
        return answer;
    }
};
