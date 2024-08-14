#include <string>
#include <unordered_set>

class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowels{'A', 'E', 'I', 'O', 'U',
                                   'a', 'e', 'i', 'o', 'u'};
        int left = 0;
        int right = s.size() - 1;
        while (true) {
            while (left < right && vowels.find(s[left]) == vowels.end())
                left += 1;
            while (left < right && vowels.find(s[right]) == vowels.end())
                right -= 1;
            if (left >= right)
                return s;
            swap(s[left], s[right]);
            left += 1;
            right -= 1;
        }
    }
};
