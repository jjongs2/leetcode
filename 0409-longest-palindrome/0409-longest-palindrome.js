/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
    const counts = {};
    for (const char of s) {
        counts[char] = (counts[char] ?? 0) + 1;
    }
    let hasCenter = false;
    const length = Object.values(counts).reduce((sum, count) => {
        hasCenter |= (count & 1);
        return sum + (count & -2);
    }, 0);
    return hasCenter ? length + 1 : length;
};
