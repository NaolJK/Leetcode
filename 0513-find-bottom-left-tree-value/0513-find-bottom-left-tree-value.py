# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        levels = defaultdict(list)
        
        q = deque([])
        
        q.append((root, 0))
        
        l = 0
        while q:
            
            node, level = q.pop()
            
            levels[level].append(node.val)
            
            if node.left:
                q.append((node.left, level + 1))
                
            if node.right:
                q.append((node.right, level+1))
            
            if node.left or node.right:
                l = max(l, level+1)
                
        return levels[l][-1]