/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
    if (n === 1) return 1;
    if (n === 2) return 2;
    const prevs = [1, 2];
    let curr;
    for (let i = 2; i < n; ++i) {
        curr = prevs.reduce((sum, prev) => sum + prev, 0);
        prevs[i & 1] = curr;
    }
    return curr;
};
