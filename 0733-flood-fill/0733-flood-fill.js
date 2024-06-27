/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, color) {
    const startColor = image[sr][sc];
    if (startColor === color) {
        return image;
    }
    image[sr][sc] = color;
    const m = image.length;
    const n = image[0].length;
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    const stack = [[sr, sc]];
    while (stack.length > 0) {
        const [r0, c0] = stack.pop();
        for (const [dr, dc] of directions) {
            const r = r0 + dr;
            const c = c0 + dc;
            if ((r < 0) || (r >= m)) continue;
            if ((c < 0) || (c >= n)) continue;
            if (image[r][c] === startColor) {
                image[r][c] = color;
                stack.push([r, c]);
            }
        }
    }
    return image;
};
