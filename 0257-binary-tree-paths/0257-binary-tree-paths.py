# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def Traverse(node,prev):
            if not node:
                return 
            if not node.right and not node.left:
                prev+=str(node.val)
                ans.append(prev)
                return
            
            prev = prev + str(node.val) + "->"
            Traverse(node.left,prev)
            Traverse(node.right,prev)
        Traverse(root,"")
        return (ans)
                
        
        