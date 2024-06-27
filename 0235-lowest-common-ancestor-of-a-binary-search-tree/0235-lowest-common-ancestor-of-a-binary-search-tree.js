/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
    const targets = new Set([p, q]);
    const findLCA = (node) => {
        if (!node) return null;
        if (targets.has(node)) return node;
        const left = findLCA(node.left);
        const right = findLCA(node.right);
        if (left && right) return node;
        return left ?? right;
    };
    return findLCA(root);
};
