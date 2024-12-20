/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int low = 0;
        int high = n;

        while (high - low > 1) {
            int mid = low + (high - low) / 2;
            if (guess(mid) > 0)
                low = mid;
            else
                high = mid;
        }
        return high;
    }
};
