# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            temp = root.right
            
            while temp.left:
                temp = temp.left
                
            root.val = temp.val
            
            root.right = self.deleteNode(root.right,temp.val)
        
        return root
        