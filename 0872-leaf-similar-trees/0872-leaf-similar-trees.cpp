/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */

#include <stack>

class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        stack<TreeNode*> s1, s2;
        s1.push(root1);
        s2.push(root2);
        while (!s1.empty() && !s2.empty()) {
            if (next_leaf(s1) != next_leaf(s2))
                return false;
        }
        return s1.empty() && s2.empty();
    }

private:
    int next_leaf(stack<TreeNode*>& s) {
        while (true) {
            TreeNode* node = s.top();
            s.pop();
            if (!node->left && !node->right)
                return node->val;
            if (node->right)
                s.push(node->right);
            if (node->left)
                s.push(node->left);
        }
    }
};
