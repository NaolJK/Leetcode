# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        
        while queue[0]:
            node = queue.popleft()
            queue.extend([node.left, node.right])
            
        while queue and not queue[0]:
            queue.popleft()
            
        return not queue