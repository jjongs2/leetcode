/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function (root) {
    const checkBalance = (node) => {
        if (!node) return 0;
        const leftDepth = checkBalance(node.left);
        if (leftDepth === -1) return -1;
        const rightDepth = checkBalance(node.right);
        if (rightDepth === -1) return -1;
        if (Math.abs(leftDepth - rightDepth) > 1) return -1;
        return Math.max(leftDepth, rightDepth) + 1;
    }
    return checkBalance(root) !== -1;
};
