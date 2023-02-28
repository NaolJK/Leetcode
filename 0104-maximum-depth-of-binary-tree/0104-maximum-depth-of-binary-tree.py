# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        right_level = self.maxDepth(root.right)
        left_level = self.maxDepth(root.left)
        
        return max(right_level, left_level) + 1 
    
    
            
        
                    
            
            
            
        
        