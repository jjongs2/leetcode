/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    const appeared = new Set();
    for (const num of nums) {
        if (appeared.has(num)) {
            return true;
        }
        appeared.add(num);
    }
    return false;
};
