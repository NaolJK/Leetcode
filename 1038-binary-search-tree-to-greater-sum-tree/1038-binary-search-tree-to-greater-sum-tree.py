# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        
        def Traverse(node, currSum):
            if not node:
                return currSum
            
            if not node.right and not node.left:
                node.val = node.val+currSum
                return node.val
            
            # print("b",node.val,currSum)
            currSum = Traverse(node.right,currSum)
            currSum+=node.val
            node.val = currSum
            # print(currSum,node.val)
            left = Traverse(node.left,currSum)
            
            return  max(currSum,left)
            
        Traverse(root,0)
        return root