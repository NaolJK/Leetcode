# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def Traverse(node):
            if not node:
                return [0,True]

            level_left,isBalanced_left = Traverse(node.left)
            
            level_right,isBalanced_right = Traverse(node.right)

            if isBalanced_left and isBalanced_right:
                
                difference = abs(level_left-level_right)
                
                if difference > 1:
                    return [max(level_left,level_right)+1, False]
                
                else:
                    return [max(level_left,level_right)+1, True]

            return [max(level_left,level_right)+1, False]
        
        return Traverse(root)[1]