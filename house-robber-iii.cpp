/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rob(TreeNode* root) {

        unordered_map<TreeNode*, int> dp;

        function <int(TreeNode*)> dfs;

        dfs = [&](TreeNode* node){
            if(!node) return 0;

            if(dp.count(node)) return dp[node];

            int rob_node = node->val;

            if(node->left){
                rob_node+= dfs(node->left->left) + dfs(node->left->right);
            }

            if(node->right){
                rob_node+=dfs(node->right->right) + dfs(node->right->left);
            }

            int rob_child = dfs(node->left) + dfs(node->right);

            int maximum = max(rob_child, rob_node);

            dp[node] = maximum;
            
            return maximum;

        };
        return dfs(root);
    }
};