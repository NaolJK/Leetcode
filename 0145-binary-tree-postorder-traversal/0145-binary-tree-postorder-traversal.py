# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        
        def PostTravesal(parent):
            if not parent:
                return 
            
            left = PostTravesal(parent.left)
            right = PostTravesal(parent.right)
            self.ans.append(parent.val)
            
        PostTravesal(root)
        return (self.ans)
        