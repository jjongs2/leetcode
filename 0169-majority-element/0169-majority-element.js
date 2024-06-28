/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
    let majorNum = 0;
    let count = 0;
    for (const num of nums) {
        if (count === 0) {
            majorNum = num;
        }
        count += (num === majorNum) ? 1 : -1;
    }
    return majorNum;
};
