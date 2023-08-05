# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        ans = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
            
        
        dfs(root)
        
        res = inf
        
        for i in range(1, len(ans)):
            res = min(res, ans[i] - ans[i-1])
        
        return res
            
            
            
        
            
        