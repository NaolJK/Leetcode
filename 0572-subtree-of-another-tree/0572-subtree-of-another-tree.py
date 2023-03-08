# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True
        
        def validate(r,s):
            if not r and not s:
                return True
            
            if r and s and r.val == s.val:
                left = validate(r.left,s.left)
                right = validate(r.right,s.right)
                return left and right
            
        ans = validate(root,subRoot)
        if ans:
            return True
        
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right,subRoot)
        
        return l or r
        