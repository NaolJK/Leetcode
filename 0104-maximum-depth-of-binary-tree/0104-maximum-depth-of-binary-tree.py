# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root,1)])
        maximum = 1
        while queue:
            node,level = queue.popleft()
            if node:
                if node.right:
                    queue.append([node.right,level+1])  
                if node.left:
                    queue.append([node.left,level+1])       
                    
        return level
                    
            
            
            
        
        