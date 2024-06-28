/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var maximumImportance = function (n, roads) {
    return roads
        .reduce((degs, [a, b]) => {
            degs[a] += 1;
            degs[b] += 1;
            return degs;
        }, Array(n).fill(0))
        .sort((deg1, deg2) => deg2 - deg1)
        .reduce((result, deg, i) => result + deg * (n - i), 0);
};
