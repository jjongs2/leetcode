/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
    const counter = {};
    for (const char of magazine) {
        counter[char] = (counter[char] ?? 0) + 1;
    }
    for (const char of ransomNote) {
        if (!counter[char]) return false;
        counter[char] -= 1;
    }
    return true;
};
