# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k, self.ans = k, 0
        
        def Traversal(node):
            if not node:
                return 
            left = Traversal(node.left)
            if self.k:
                self.ans = node.val
                self.k-=1
            right = Traversal(node.right)
            
        Traversal(root)
        return self.ans
        
            
            
        