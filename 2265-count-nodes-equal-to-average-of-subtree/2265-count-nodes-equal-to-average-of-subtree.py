# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if not node:
                return [0 ,0, 0]
            
            if not node.right and not node.left:
                return [1, 1, node.val]
            
            l_count,l_c,left = traverse(node.left)
            r_count,r_c,right = traverse(node.right)
            
            tot_count = l_count + r_count + 1
            summation = left + right + node.val
            average = (summation)//(tot_count)
            ans = l_c+r_c
            if (average) == node.val:
                ans+=1
                
            return [tot_count, ans, summation]
        
        return (traverse(root)[1])
            
        