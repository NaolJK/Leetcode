# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        ans = defaultdict(list)
        row = 0
        queue = deque([(root,0,row)])
        
        while queue:
            node, level,row = queue.popleft()
            
            ans[level].append((row,node.val))  
            
            if node.left:
                queue.append((node.left,level-1 , row+1))
            if node.right:
                queue.append((node.right, level+1, row+1))
        res = []
        
        ans = (sorted(ans.items()))
        for key, val in ans:
            r = [value for i,value in sorted(val)]
            res.append(r)
        return (res)
            
            
            
            
        
            
        
        