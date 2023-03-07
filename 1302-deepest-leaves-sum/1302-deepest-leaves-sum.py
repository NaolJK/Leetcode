# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        
        def Deepest(node):
            if not node:
                return [0,0]
            
            if not node.right and not node.left:
                return [node.val,1]
            
            left,l_count = Deepest(node.left)
            right,r_count = Deepest(node.right)
            
            if l_count == r_count:
                return [left+right,l_count+1]
            
            elif l_count > r_count:
                return [left,l_count+1]
            
            else:
                return [right,r_count+1]
            
        return Deepest(root)[0]
            
        