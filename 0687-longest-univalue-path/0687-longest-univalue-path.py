# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def longest(node):
            if not node:
                return [0,0]
            
            count_l,maximum_l = longest(node.left)
            count_r,maximum_r = longest(node.right)
            
            
            if node.left and node.right and node.left.val == node.val == node.right.val:
                summation = count_l + count_r + 1
                return [max(count_l,count_r)+1,max(maximum_l,maximum_r,summation)]
            elif node.left and node.left.val == node.val:
                summation = count_l + 1
                return [summation,max(maximum_l,maximum_r,summation)]
            elif node.right and node.right.val == node.val:
                summation = count_r + 1
                return [summation,max(maximum_l,maximum_r,summation)]
            else:
                return [1,max(maximum_l,maximum_r,1)]
                
        return longest(root)[1] - 1