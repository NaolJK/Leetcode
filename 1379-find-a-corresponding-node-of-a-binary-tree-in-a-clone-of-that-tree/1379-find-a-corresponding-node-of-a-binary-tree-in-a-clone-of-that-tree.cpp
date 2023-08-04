/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {     
        
        if(!cloned) return NULL;
        
        if(original == target) return cloned;
        
        TreeNode* left_val = getTargetCopy(original->left,cloned->left,target);
        
        TreeNode* right_val = getTargetCopy(original->right,cloned->right,target);
        
        if(left_val) return left_val;
        if(right_val) return right_val;
        return NULL;
    }
};