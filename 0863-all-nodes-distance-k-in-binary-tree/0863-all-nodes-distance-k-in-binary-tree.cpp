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
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        
        vector <int> graph[500];
        
        function <void(TreeNode*)> convert = [&](TreeNode* tree){
            if(!tree){
                return;
            }
            
            if(tree->left){
                graph[tree->val].push_back(tree->left->val);
                graph[tree->left->val].push_back(tree->val);
            }
            
            if(tree->right){
                graph[tree->val].push_back(tree->right->val);
                graph[tree->right->val].push_back(tree->val);
            }
            convert(tree->left);
            convert(tree->right);
        };
        
        convert(root);
        queue<int> q;
        q.push(target->val);
        vector <bool> seen(500);
        seen[target->val] = true;
        int level = 0;
        vector <int> ans;
        
        while(!q.empty()){
            int length = q.size();
            ++level;
            for(int i=0; i <length; ++i){
                int node = q.front();
                q.pop();
                if(level == k+1){
                    ans.push_back(node);
                }
                for(auto v : graph[node]){
                    if(seen[v]) continue;
                    q.push(v);
                    seen[v] = true;
                }
            }
        }
        
        return ans;
    }
};