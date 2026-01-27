class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;
        int digit;
        int sum;

        while (seen.find(n) == seen.end()) {
            if (n == 1) {
                return true;
            }
            seen.insert(n);
            sum = 0;
            while (n > 0) {
                digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            n = sum;
        }
        return false;
    }
};
