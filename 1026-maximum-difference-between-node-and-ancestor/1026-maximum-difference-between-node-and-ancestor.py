# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0

        def dfs(node, mn, mx):
            
            mx = max(mx, node.val)
            
            mn = min(mn, node.val)
            
            self.ans = max( self.ans , abs( mx - mn ) )
            
            if node.left:
                
                dfs(node.left, mn, mx)
                
            if node.right:
                
                dfs(node.right, mn, mx)
                
        
        dfs(root, root.val, root.val)

        return self.ans