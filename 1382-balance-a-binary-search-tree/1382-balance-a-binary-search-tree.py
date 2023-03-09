# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lists = []
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            lists.append(node.val)
            traverse(node.right)
        
        traverse(root)
        
        def insertToNode(left,right):
            if left > right:
                return 
            middle = (left+right)//2
            new_node = TreeNode(lists[middle])
            
            new_node.left = insertToNode(left,middle-1)
            new_node.right = insertToNode(middle+1, right)
            return new_node
        return insertToNode(0, len(lists)-1)
        