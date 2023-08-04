# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        
        def dfs(node, l):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [node.val]
            
            left = dfs(node.left, l)
            right = dfs(node.right, l)
            
            ans = [*l,*left, *right]
            
            return ans
        
        l1 = dfs(root1, [])
        l2 = dfs(root2, [])
        
        return l1 == l2
                
        