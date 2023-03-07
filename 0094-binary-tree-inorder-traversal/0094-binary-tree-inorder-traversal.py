# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        
        def InorderTravesal(parent):
            
            if not parent:
                return 
            
            left = InorderTravesal(parent.left)
            self.ans.append(parent.val)
            right = InorderTravesal(parent.right)
            
        InorderTravesal(root)
        return (self.ans)