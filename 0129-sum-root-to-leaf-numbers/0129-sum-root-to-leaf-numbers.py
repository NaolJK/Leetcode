# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def traverse(node, string):
            if not node:
                return
            if not node.left and not node.right:
                ans.append(int(string+str(node.val)))
                return 
            
            traverse(node.left, string+ str(node.val))
            traverse(node.right, string+ str(node.val))
        traverse(root,"")
        
        return sum(ans)
            
            
            
        