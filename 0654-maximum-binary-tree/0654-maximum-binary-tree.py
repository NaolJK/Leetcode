# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def divide(i,j):
            if i > j:
                return
            maximum = nums[i]
            idx = i
            for k in range(i+1,j+1):
                if maximum < nums[k]:
                    idx =k
                    maximum = nums[k]
            new_node = TreeNode(maximum)
            new_node.left = divide(i,idx-1)
            new_node.right = divide(idx+1,j)
            return new_node
        return divide(0,len(nums)-1)
                
                