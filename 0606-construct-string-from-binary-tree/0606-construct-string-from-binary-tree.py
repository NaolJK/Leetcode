# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        self.ans = ""
        def dfs(node):
            
            if not node:
                return
            
            self.ans+="("
            self.ans+=str(node.val)
            
            dfs(node.left)
            if(not node.left and node.right):
                self.ans+="()"
            dfs(node.right)
            self.ans+=")"
            
            
            
        dfs(root)
        
        return self.ans[1:-1]
            
            
            
        