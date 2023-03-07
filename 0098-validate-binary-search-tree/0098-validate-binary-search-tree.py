# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = []
        def Inorder(node):
            if not node:
                return 
            
            Inorder(node.left)
            ans.append(node.val)
            Inorder(node.right)
            
        Inorder(root)
        # print(ans)
        for i in range(1,len(ans)):
            if ans[i] <= ans[i-1]:
                # print(ans[i])
                return False
            
        return True
       
        
        
        
        
        
        