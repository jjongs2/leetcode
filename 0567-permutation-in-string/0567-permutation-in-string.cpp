class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.size();
        int n2 = s2.size();

        if (n1 > n2) {
            return false;
        }

        int left = 0;
        int right = 0;
        array<int, 26> freq1{{}};
        array<int, 26> freq2{{}};

        while (right < n1) {
            freq1[s1[right] - 'a'] += 1;
            freq2[s2[right] - 'a'] += 1;
            right += 1;
        }
        while (right < n2) {
            if (freq1 == freq2) {
                return true;
            }
            freq2[s2[left] - 'a'] -= 1;
            freq2[s2[right] - 'a'] += 1;
            left += 1;
            right += 1;
        }
        return freq1 == freq2;
    }
};
