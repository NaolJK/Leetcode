# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lowest(node):
            if not node:
                return [False,None]
            
            L,LN = lowest(node.left)
            R,RN = lowest(node.right)
            
            if node == p or node == q:
                if R or L:
                    return [True,node]
                else:
                    return [True,None]
            else:
                if R and L:
                    return [True,node]
                
                elif R or L:
                    return [True, LN if L else RN]
                
                return [False,None]
            
        return lowest(root)[1]