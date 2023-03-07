# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k, self.ans = k, 0
        
        def Traversal(node,count):
            
            if not node:
                return [0,-1]
            # if count = k:
                # return [count,node.val]
            
            left, ans = Traversal(node.left,count)
            
            if left+1+count==k:
                ans = node.val
            right = 0
           
            if ans==-1:
                right, ans = Traversal(node.right,count+left+1)
            
            
            # print(count,node.val,ans)
            return [left+right+1, ans]
                
            
            
            
        a,b = Traversal(root,0)
        return b
        
            
            
        