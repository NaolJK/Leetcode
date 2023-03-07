# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def Traverse(node1,node2):
            
            if not node1 and node2:
                new_node = TreeNode(node2.val)
                new_node.right = node2.right
                new_node.left = node2.left
                return new_node
            
            if not node1 and not node2:
                return 
            
            if not node1 and not node2:
                return 
            
            if node1 and node2:
                node1.val = node1.val + node2.val
                node1.left = Traverse(node1.left,node2.left)
                node1.right = Traverse(node1.right,node2.right)
            return node1
        
        
        return Traverse(root1,root2)
            
        