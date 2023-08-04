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
    vector<int> inorderTraversal(TreeNode* root) {
        
        vector<int> ans;
        
        function<void(TreeNode*)> dfs = [&](TreeNode* node){
          if(!node) return;
            
          dfs(node->left);
          ans.push_back(node->val);
          dfs(node->right);
        };
        dfs(root);
        
        return ans;
    }
};