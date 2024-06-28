/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var maximumImportance = function (n, roads) {
    const degrees = new Array(n).fill(0);
    for (const [a, b] of roads) {
        degrees[a] += 1;
        degrees[b] += 1
    }
    let totalImportance = 0;
    degrees.sort((d1, d2) => d2 - d1);
    degrees.forEach((degree, index) => {
        totalImportance += degree * (n - index);
    });
    return totalImportance;
};
