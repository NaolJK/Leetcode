# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def dfs(node):
            
            # nonlocal ans
            
            if not node:
                return 0
            
            if not node.left and not node.right:
                
                return node.val
            
            left = dfs(node.left)
            
            right = dfs(node.right)
            
            self.ans+= (abs(left - right))
            
            # print(left, right)
            return node.val + left + right
        
        dfs(root)
        
        return self.ans
            
            
            
            
        