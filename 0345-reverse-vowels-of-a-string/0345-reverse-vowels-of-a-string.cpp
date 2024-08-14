#include <algorithm>
#include <string>

class Solution {
public:
    string reverseVowels(string s) {
        const string VOWELS = "AEIOUaeiou";
        int left = -1;
        int right = s.size();
        while (true) {
            left = s.find_first_of(VOWELS, left + 1);
            right = s.find_last_of(VOWELS, right - 1);
            if (left >= right)
                return s;
            swap(s[left], s[right]);
        }
    }
};
