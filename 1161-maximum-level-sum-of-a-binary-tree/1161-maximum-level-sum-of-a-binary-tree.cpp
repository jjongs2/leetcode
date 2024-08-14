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

#include <limits>
#include <queue>

class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        int max_sum = numeric_limits<int>::min();
        int max_level = 1;
        int level = 0;
        queue<TreeNode*> q{{root}};

        while (!q.empty()) {
            level += 1;
            int sum = 0;
            for (int i = q.size(); i > 0; --i) {
                TreeNode* node = q.front();
                q.pop();
                sum += node->val;
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }
            if (sum > max_sum) {
                max_sum = sum;
                max_level = level;
            }
        }
        return max_level;
    }
};
