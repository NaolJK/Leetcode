# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node, c):
            if not node:
                return 0
            
            if not node.left and not node.right and c:
                return node.val
            
            left = dfs(node.left, 1)
            
            right = dfs(node.right, 0)
            
            return left + right
        
        return dfs(root,0)