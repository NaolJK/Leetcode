# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def getParent(node,val):
            if node.val == val:
                return [node]
            
            elif node.val > val:
                ans = getParent(node.left,val)
                ans.append(node)
                return ans 
                    
                
            elif node.val < val:
                ans = getParent(node.right,val)
                ans.append(node)
                return ans
        
        parent_one = (getParent(root, p.val))
        parent_two = (getParent(root, q.val))
        for node in parent_one:
            if node in parent_two:
                return node
        
      
        
        
        